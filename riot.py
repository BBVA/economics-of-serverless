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


# https://aws.amazon.com/lambda/pricing/?nc1=h_ls
class Lambda(object):
    price_per_million_reqs = .20
    price_per_GB_s = .00001667
    free_tier_reqs = 1000000
    free_tier_GB_s = 400000
    ms_per_req = 0
    mem = 0

    valid_lambda_mem = set(list([
        128, 192, 256, 320, 384, 448, 512, 576,
        640, 704, 768, 832, 896, 960, 1024, 1088,
        1152, 1216, 1280, 1344, 1408, 1472, 1536
    ]))

    def __init__(self, mem=128, ms_per_req=100):
        self.mem = mem
        if mem not in self.valid_lambda_mem:
            self.mem = 128

        self.ms_per_req = ms_per_req

    def _costs_compute(self, reqs):
        # Total compute (seconds) = 3M * (1s) = 3,000,000 seconds
        total_compute_seconds = reqs * self.ms_per_req / 1000
        # Total compute (GB-s) = 3,000,000 * 512MB/1024 = 1,500,000 GB-s
        total_compute_gb_s = total_compute_seconds * self.mem / 1024
        # Total compute – Free tier compute = Monthly billable compute GB- s
        total_compute = total_compute_gb_s - self.free_tier_GB_s

        return max(0, total_compute * self.price_per_GB_s)

    def _costs_request(self, reqs):

        # Total requests – Free tier requests = Monthly billable requests
        monthly_billable_requests = reqs - self.free_tier_reqs
        # 3M requests – 1M free tier requests = 2M Monthly billable requests
        # 1,500,000 GB-s – 400,000 free tier GB-s = 1,100,000 GB-s

        return max(0, (monthly_billable_requests * self.price_per_million_reqs) / 1000000)

    def cost(self, reqs):
        return self._costs_compute(reqs) + self._costs_request(reqs)


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
    device_number = 0
    request_period_in_seconds = 0
    period_start = 0
    period_end = 0
    resolution_in_seconds = 0
    MB_per_req = 0
    ms_per_req = 0
    myLambda = ""
    myEC2 = ""

    def __init__(self, n, p, s, e, r, pr, mr, mb, ms):
        self.device_number = n
        self.request_period_in_seconds = p
        self.period_start = s
        self.period_end = e
        self.resolution_in_seconds = r
        self.MB_per_req = mb
        self.ms_per_req = ms

        self.myLambda = Lambda(mb, ms)
        self.myEC2 = EC2(pr, mr)


def new_model(n, p, d, r, i, mr, mb, ms):
    today = datetime.today()
    start = datetime(today.year, 1, 1)
    end = start + timedelta(days=d)
    return Model(n, p, start, end, r, i['hourly_price'], mr, mb, ms)


def generate(model):
    # Create device fleet generator (lazy generates a collection of time deltas)
    devices = devices_generator(
        model.device_number, model.request_period_in_seconds)

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
        lc = model.myLambda.cost(acc)
        ni = max(1, model.myEC2.get_n_instances(reqs))
        ec = model.myEC2.cost(hours) * ni
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
    device_count_list = [10, 100, 1000, 10000, 100000, 1000000, 10000000]
    print("df_len,hits,lambda,ec2,freq,instance_count")
    for freq in req_freq_list:
        for device_count in device_count_list:
            instance = ec2_instances['m4.4xlarge']
            resolution_in_seconds = 60
            period_in_days = 30
            lambda_memory = 128
            request_duration_ms = 200

            max_concurrent_requests = get_ec2_max_concurrent_reqs(instance, lambda_memory, resolution_in_seconds)
            model = new_model(device_count, freq, period_in_days, resolution_in_seconds, instance, max_concurrent_requests, lambda_memory, request_duration_ms)

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
