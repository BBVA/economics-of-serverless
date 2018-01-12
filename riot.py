import math
import json
import numpy as np
import pandas as pd

from datetime import datetime
from functools import reduce
from itertools import groupby, chain
from random import randint
from datetime import timedelta
from iot.simulator import *

import awscosts


class EC2(object):
    cost_per_hour = 0
    max_concurrent_reqs = 0
    price_per_hour = 0

    def __init__(self, price_per_hour, max_concurrent_reqs):

        self.price_per_hour = float(price_per_hour)
        self.max_concurrent_reqs = max_concurrent_reqs

    def cost(self, hours):
        return self.price_per_hour * hours

    def get_n_instances(self, reqs):
        return math.ceil(reqs / self.max_concurrent_reqs)


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


def new_model(num_devices, request_period, num_days, resolution, ec2_price_per_hour, ec2_max_concurrent_reqs, lambda_mb_per_req, lambda_ms_per_req):
    today = datetime.today()
    period_start = datetime(today.year, 1, 1)
    period_end = period_start + timedelta(days=num_days)
    lambda_instance = awscosts.Lambda(lambda_mb_per_req, lambda_ms_per_req)
    ec2_instance = EC2(ec2_price_per_hour, ec2_max_concurrent_reqs)
    return Model(num_devices, request_period, period_start, period_end, resolution, lambda_instance, ec2_instance)


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
        hours = model.resolution_in_seconds / 3600
        lc = model.lambda_instance.get_cost(acc, reset_free_tier=True)
        ni = max(1, model.ec2_instance.get_n_instances(reqs))
        ec = model.ec2_instance.cost(hours) * ni
        acc = acc + x['hits']
        return x['date'], x['hits'], acc, lc, ec, ni

    df['hits_acc'] = 0
    df['lambda_cost'] = 0
    df['ec2_cost'] = 0
    df['instances'] = 0
    df[['date', 'hits', 'hits_acc', 'lambda_cost',
        'ec2_cost', 'instances']] = df.apply(myl, axis=1)

    return df


def get_ec2_prices():
    resource_path = '/'.join(('awscosts', 'awscosts', 'ec2prices.json'))
    # data[instance_type]['memory']
    # data[instance_type]['hourly_price']
    return json.load(open(resource_path))


def get_ec2_max_concurrent_reqs(flavour, mb_per_req, res):
    return float(flavour['memory']) * 1024 / mb_per_req * res


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
    ec2_instances = get_ec2_prices()
    req_freq_list = [3600, 8 * 3600, 24 * 3600]
    device_count_list = [10, 100, 1000, 10000, 100000,
                         1000000, 10000000, 100000000, 1000000000, 10000000000]
    print("df_len,hits,lambda,ec2,freq,instance_count")
    for freq in req_freq_list:
        for device_count in device_count_list:
            instances = (
                ec2_instances['t2.large'], ec2_instances['m4.large'], ec2_instances['m4.4xlarge'])
            resolution_in_seconds = 60
            period_in_days = 30
            lambda_memory = 128
            request_duration_ms = 200
			
            for instance in instances:
                max_concurrent_requests = get_ec2_max_concurrent_reqs(instance, lambda_memory, resolution_in_seconds)
                model = new_model(device_count, freq, period_in_days, resolution_in_seconds, instance['hourly_price'], max_concurrent_requests, lambda_memory, request_duration_ms)
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
