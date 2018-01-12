import json
import pandas as pd

from datetime import datetime
from functools import reduce
from itertools import groupby, chain
from datetime import timedelta
from iot.simulator import *

import awscosts


class Model(object):
    num_devices = 0
    request_period_in_seconds = 0
    period_start = 0
    period_end = 0
    resolution_in_seconds = 0
    lambda_instance = None
    ec2_instance = None

    def __init__(self, num_devices, request_period, period_start, period_end, resolution, lambda_instance, ec2_instance):
        self.num_devices = num_devices
        self.request_period_in_seconds = request_period
        self.period_start = period_start
        self.period_end = period_end
        self.resolution_in_seconds = resolution
        self.lambda_instance = lambda_instance
        self.ec2_instance = ec2_instance


def new_model(num_devices, request_period, num_days, resolution,
              ec2_flavor, lambda_mb_per_req, lambda_ms_per_req):

    today = datetime.today()
    period_start = datetime(today.year, 1, 1)
    period_end = period_start + timedelta(days=num_days)
    lambda_instance = awscosts.Lambda(lambda_mb_per_req, lambda_ms_per_req)
    ec2_instance = awscosts.EC2(ec2_flavor, MB_per_req=lambda_mb_per_req,
                                ms_per_req=lambda_ms_per_req)

    return Model(num_devices, request_period, period_start, period_end,
                 resolution, lambda_instance, ec2_instance)


def generate(model):
    # Create device fleet generator (lazy generates a collection of time deltas)
    devices = devices_generator(
        model.num_devices, model.request_period_in_seconds)

    # Create a generator for device periodic requests
    request_period_generator = time_walker(
        model.period_start, model.request_period_in_seconds, model.period_end)

    # Create a "stamper" that fixes deltas into actual datetime stamps for a specific period
    stamper = devices_date_stamper(devices)

    # Create a function that returns the t0 of a period for a given time
    resolution_finder = resolution_period_finder(
        model.period_start, model.resolution_in_seconds)

    # flatMap = map + reduce
    all_requests = reduce(chain, map(
        stamper, request_period_generator), iter([]))

    requests_by_resolution = map(lambda x: (
        x[0], len(list(x[1]))), groupby(all_requests, resolution_finder))

    return pd.DataFrame.from_records(list(requests_by_resolution), index='date', columns=['date', 'hits'])


def costs(model, df):

    df['date'] = df.index

    acc = 0

    def myl(x):
        nonlocal acc
        reqs = x['hits']
        lc = model.lambda_instance.get_cost(acc, reset_free_tier=True)
        ni = max(1, model.ec2_instance.get_num_instances(
            reqs/model.resolution_in_seconds))
        ec = model.ec2_instance.get_cost(model.resolution_in_seconds) * ni
        acc = acc + x['hits']
        return x['date'], x['hits'], acc, lc, ec, ni

    df['hits_acc'] = 0
    df['lambda_cost'] = 0
    df['ec2_cost'] = 0
    df['instances'] = 0
    df[['date', 'hits', 'hits_acc', 'lambda_cost',
        'ec2_cost', 'instances']] = df.apply(myl, axis=1)

    return df


class DateTimeEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime):
            return o.isoformat()
        if isinstance(o, Lambda):
            return o.__dict__
        if isinstance(o, EC2):
            return o.__dict__

        return json.JSONEncoder.default(self, o)


def main():
    req_freq_list = [3600, 8 * 3600, 24 * 3600]
    device_count_list = [10, 100, 1000, 10000, 100000,
                         1000000, 10000000, 100000000, 1000000000, 10000000000]
    print("df_len,hits,lambda,ec2,freq,instance_count")
    for freq in req_freq_list:
        for device_count in device_count_list:
            flavors = ('t2.large', 'm4.large', 'm4.4xlarge')
            resolution_in_seconds = 60
            period_in_days = 30
            lambda_memory = 128
            request_duration_ms = 200

            for flavor in flavors:
                model = new_model(device_count, freq, period_in_days,
                                  resolution_in_seconds,
                                  flavor, lambda_memory,
                                  request_duration_ms)
                # print(json.dumps(model.__dict__,
                #                cls=DateTimeEncoder, indent=2, sort_keys=True))

                df = costs(model, generate(model))
                v = df.tail(1).index.item()
                result = [len(df.index), df["hits"].sum(), df.get_value(v, 'lambda_cost'),
                         df["ec2_cost"].sum(), freq, df['instances'].max()]

                print(','.join(map(str, result)))
                # print(df.tail())


if __name__ == "__main__":
    main()
