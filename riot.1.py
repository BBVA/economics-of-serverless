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

from functools import reduce, partial
import plotly
import plotly.graph_objs as go
import awscosts
from bbva_colors import BBVAcolors


def aggregate_costs(
    req_period,
    resolution,
    interval_duration,
    num_devices,
    lambda_instance,
    ec2_instances_list,
    # devices_time_series,
):

    # Generate Time Series:
    mean = num_devices // req_period
    time_series = list()
    for i in range(0, (interval_duration // resolution)):
        if i > 0 and i < 1000:
            time_series.append(mean / 2)
        if i >= 1000 and i < 1500:
            time_series.append(mean * 2)
        if i >= 1500 and i < 6500:
            time_series.append(mean / 2)
        if i >= 6500 and i < 8000:
            time_series.append(mean * 2)
        if i >= 8000:
            time_series.append(mean / 2)

    costs = {}
    costs['resolution_buckets'] = interval_duration // resolution
    costs['hits'] = num_devices * (interval_duration // req_period)
    costs['reqs_per_second'] = costs['hits'] / interval_duration
    costs['lambda'] = lambda_instance.get_cost(
        costs['hits'],
        reset_free_tier=True
    )

    def calc_ec2_instance_use(num_hits, ec2_instance, resolution=0):
        return ec2_instance.get_cost_and_num_instances(
            resolution,
            num_hits * resolution,
        )

    for ec2_instance in ec2_instances_list:
        calc_by_instance = partial(
            calc_ec2_instance_use,
            ec2_instance=ec2_instance,
            resolution=resolution
        )

        cost, instances = reduce(
            lambda x, y: (
                x[0] + y[0], max(x[1], y[1])
            ),
            map(calc_by_instance, time_series),
            (0, 0)
        )

        costs.update({
            f'ec2_{ec2_instance._instance_type}_cost': cost,
            f'ec2_{ec2_instance._instance_type}_instances': instances
        })

    return costs


def draw_costs_by_num_devices(
    costs,
    num_devices_list,
    ec2_flavors,
    req_period
):

    data = []

    lambda_trace = go.Scatter(
        x=[cost["reqs_per_second"] for cost in costs],
        y=[cost['lambda'] for cost in costs],
        name='Lambda',
        marker=BBVAcolors['coral']
    )
    data.append(lambda_trace)

    for flavor, color in zip(ec2_flavors, ['light', 'aqua', 'navy']):
        trace = go.Scatter(
            x=[cost["reqs_per_second"] for cost in costs],
            y=[cost[f'ec2_{flavor}_cost'] for cost in costs],
            name=f'EC2 {flavor}',
            marker=BBVAcolors[color]
        )
        data.append(trace)

    layout = go.Layout(
        title=f'<b>Monthly cost by number of requests per second</b><br>' +
        f'<i>(request period: {req_period} seconds)</i></b>',
        legend=dict(orientation='h'),
        width=1000,
        height=800,
        xaxis=dict(
            title='<b>Number of reqs/sec</b>',
            type='log'
        ),
        yaxis=dict(
            title='<b>Monthly cost ($)</b>',
            type='log'
        )
    )

    fig = go.Figure(data=data, layout=layout)
    plotly.offline.plot(fig)


def main():

    def devices_func(acc, i):
        if i % 2 == 0:
            acc.append(acc[i-1] * 2)
        else:
            acc.append(acc[i-1] * 5)
        return acc

    ec2_flavors = ('m3.medium', 'm4.large', 'm4.4xlarge')
    req_period_list = [3600]  # , 8* 3600, 24 * 3600]
    # [10, 50, 100, 500, 1000, 5000, 10000, 50000, 100000, 500000, 1000000,
    # 5000000, 10000000]
    num_devices_list = reduce(devices_func, range(1, 13), [10])
    num_devices_list = list(range(200000, 10000000, 100000))
    resolution = 60 * 5  # in seconds
    interval_duration = 30 * 24 * 3600  # one month in seconds
    lambda_memory = 128
    lambda_request_duration_ms = 200
    ec2_instances = [awscosts.EC2(
        flavor,
        MB_per_req=lambda_memory,
        ms_per_req=lambda_request_duration_ms
    ) for flavor in ec2_flavors]

    for req_period in req_period_list:
        costs = []
        for num_devices in num_devices_list:
            lambda_instance = awscosts.Lambda(
                lambda_memory,
                lambda_request_duration_ms
            )
            cost = aggregate_costs(
                req_period,
                resolution,
                interval_duration,
                num_devices,
                lambda_instance,
                ec2_instances,
            )

            print(
                cost['hits'],
                cost['reqs_per_second'],
                cost['lambda'],
                cost['ec2_m3.medium_cost'] * cost[f'ec2_m3.medium_instances'],
                cost['ec2_m4.large_cost'] * cost[f'ec2_m4.large_instances'],
                cost['ec2_m4.4xlarge_cost'] * cost[f'ec2_m4.4xlarge_instances']
            )

            costs.append(cost)

        draw_costs_by_num_devices(
            costs,
            num_devices_list,
            ec2_flavors,
            req_period
        )


if __name__ == "__main__":
    main()
