# Copyright 2018 BBVA
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import awscosts
import pandas as pd
import datetime
import numpy as np


def simulate(df: pd.DataFrame, monthly_scale_factor=None):

    # prepare DF fields
    df['hits'] = df['hits'].astype(float)
    df['weekday'] = df.index.weekday_name
    df['hour'] = df.index.hour

    startdate = datetime.datetime(2018, 1, 7)
    days = ('Monday', 'Tuesday', 'Wednesday', 'Thursday',
            'Friday', 'Saturday', 'Sunday')

    week_df = pd.DataFrame()

    for day in days:
        aux_df = pd.DataFrame(
            index=pd.date_range(start=startdate, periods=24, freq='H'),
            columns=['requests']
        )

        # Create a list of average hits for each hour in a given weekday:
        hitmeans = df.loc[df['weekday'] == day].groupby('hour')['hits'].mean()
        aux_df['requests'] = np.array(hitmeans).round().astype(int)
        startdate += datetime.timedelta(days=1)
        week_df = pd.concat([week_df, aux_df])

    # Build 35-days DataFrame from week DF
    month_df = pd.DataFrame(
        index=pd.date_range(
            start=datetime.datetime(2018, 1, 1), periods=35 * 24, freq='H'
        )
    )
    month_df['requests'] = list(week_df['requests']) * 5

    # Delete last 5 days to get 30 days (1 month)
    month_df = month_df.drop(month_df.index[-120:])

    total_month_hits = float(month_df['requests'].sum())
    month_df['reqs_normalized'] = \
        month_df['requests'] / total_month_hits

    if monthly_scale_factor is not None:
        month_df['requests'] = \
            month_df['reqs_normalized'] * monthly_scale_factor
        month_df = month_df.round({'requests': 0})
        month_df['requests'] = month_df['requests'].astype(int)

    month_df['req_sum'] = month_df.requests.cumsum()

    return month_df


def get_lambda_cost(df: pd.DataFrame, MB_per_request=128, ms_per_req=200):
    mylambda = awscosts.Lambda(
        MB_per_req=MB_per_request,
        ms_per_req=ms_per_req
    )

    df['lambda_cost'] = df.apply(
        lambda x: mylambda.get_cost(reqs=x['requests']),
        axis=1
    )

    df['lambda_sum'] = df.lambda_cost.cumsum()
    df = df.round({'lambda_cost': 2, 'lambda_sum': 2})

    return df


def get_ec2_cost(df: pd.DataFrame, flavor, **kwargs):

    myec2 = awscosts.EC2(instance_type=flavor, **kwargs)
    df[flavor] = df.apply(
        lambda x: myec2.get_cost_and_num_instances(3600, reqs=x['requests'])[0],
        axis=1
    )

    df[flavor + '_instances'] = df.apply(
        lambda x: myec2.get_num_instances(reqs=x['requests'] / 3600),
        axis=1
    )

    df[flavor + '_sum'] = df[flavor].cumsum()
    df = df.round({flavor: 2, flavor + '_sum': 2})
    return df


def find_breakeven(df: pd.DataFrame, flavor):
    # df['req_sum'] = df.requests.cumsum()
    breakeven_df = df[df[flavor + '_break_even'] > 0]
    if breakeven_df.empty:
        return None
    # print(breakeven_df.head())

    return breakeven_df['req_sum'][0]


def get_monthly_cost(
    requests_df: pd.DataFrame,
    factor_list: list,
    ec2_flavors: dict,
    lambda_flavor: dict,
    throughput_ratio=1,
):
    # simulate and calculate costs for several factors:
    cost_points = dict.fromkeys(ec2_flavors + ('lambda', ))
    cost_points['lambda'] = list()
    for flavor in ec2_flavors:
        cost_points[flavor] = list()

    for factor in factor_list:
        month_df = simulate(requests_df, monthly_scale_factor=factor)

        # calculate costs for Lambda:
        month_df = get_lambda_cost(
            month_df,
            MB_per_request=lambda_flavor['memory'],
            ms_per_req=lambda_flavor['exec_time'],
        )

        cost_points['lambda'].append(
            month_df['lambda_sum'].iloc[-1]
        )

        # calculate costs for EC2 instances:
        for flavor in ec2_flavors:
            month_df = get_ec2_cost(
                month_df,
                flavor=flavor,
                MB_per_req=lambda_flavor['memory'],
                ms_per_req=lambda_flavor['exec_time'],
                throughput_ratio=throughput_ratio,
            )

            cost_points[flavor].append(
                month_df[f'{flavor}_sum'].iloc[-1]
            )

    mean_reqs_per_second = [x / float(28 * 24 * 60 * 60) for x in factor_list]
    return list(mean_reqs_per_second), cost_points


def get_breakeven(
    df: pd.DataFrame,
    factor_list: list,
    ec2_flavors: dict,
    lambda_flavor: dict,
    throughput_ratio=1,
):
    # simulate and calculate costs for several factors:
    breakeven_points = dict()
    for factor in factor_list:
        month_df = simulate(df, monthly_scale_factor=factor)

        month_df = get_lambda_cost(
            month_df,
            MB_per_request=lambda_flavor['memory'],
            ms_per_req=lambda_flavor['exec_time'],
        )

        for flavor in ec2_flavors:
            month_df = get_ec2_cost(
                month_df,
                flavor=flavor,
                MB_per_req=lambda_flavor['memory'],
                ms_per_req=lambda_flavor['exec_time'],
                throughput_ratio=throughput_ratio,
            )

            month_df[flavor + '_break_even'] = \
                month_df['lambda_sum'] - month_df[flavor + '_sum']

            breakeven = find_breakeven(month_df, flavor)

            if flavor not in breakeven_points.keys():
                breakeven_points[flavor] = list()
            if breakeven is not None:
                breakeven_points[flavor].append(
                    (breakeven / factor) * 100
                )
            else:
                breakeven_points[flavor].append(100)

    mean_reqs_per_second = [x / float(28 * 24 * 60 * 60) for x in factor_list]
    return list(mean_reqs_per_second), breakeven_points
