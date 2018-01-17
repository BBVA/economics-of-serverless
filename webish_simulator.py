# FIXME: datetime.now() has to be replaced with the last monday at 0:00
# TODO: crear df de 30 días y meterle la semana sintética tantas veces como entre
# TODO: ya no es necesario trabajar con datetimes
# TODO: separar funcion que calcula costes en el DF

import awscosts
import pandas as pd
import datetime
import numpy as np

# IMMEDIATE TODO: have lunch and then extract the cost calculations into its own
# function

def simulate(
        df: pd.DataFrame,
        monthly_scale_factor=None,
        MB_per_request=512,
        ms_per_req=200,
        max_reqs_per_second=1000
    ):
    # need to convert types to avoid a INF value while computing mean value
    # (too big number?)
    # prepare DF fields
    df['hits'] = df['hits'].astype(float)
    df['weekday'] = df.index.weekday_name
    df['hour'] = df.index.hour

    startdate = datetime.datetime(1970, 1, 5)
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

    # Build month DataFrame from week DF
    month_df = pd.DataFrame(
        index=pd.date_range(
            start=datetime.datetime(2018, 1, 1), periods=28 * 24, freq='H'
        )
    )
    month_df['requests'] = list(week_df['requests']) * 4
    total_month_hits = float(month_df['requests'].sum())
    month_df['reqs_normalized'] = \
        month_df['requests'] / total_month_hits

    if monthly_scale_factor is not None:
        month_df['requests'] = \
            month_df['reqs_normalized'] * monthly_scale_factor
        month_df = month_df.round({'requests': 0})
        month_df['requests'] = month_df['requests'].astype(int)

    mylambda = awscosts.Lambda(
        MB_per_req=MB_per_request,
        ms_per_req=ms_per_req
    )
    myec2 = awscosts.EC2(
        instance_type='t2.large',
        max_reqs_per_second=max_reqs_per_second
    )

    month_df['lambda_cost'] = month_df.apply(
        lambda x: mylambda.get_cost(reqs=x['requests']),
        axis=1
    )

    month_df['ec2_cost'] = month_df.apply(
        lambda x: myec2.get_cost_and_num_instances(3600, reqs=x['requests'])[0],
        axis=1
    )

    month_df['instances'] = month_df.apply(
        lambda x: myec2.get_num_instances(reqs=x['requests'] / 3600),
        axis=1
    )
    month_df['lambda_sum'] = month_df.lambda_cost.cumsum()
    month_df['ec2_sum'] = month_df.ec2_cost.cumsum()

    return month_df
