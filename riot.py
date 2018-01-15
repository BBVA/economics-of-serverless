from functools import reduce
from itertools import groupby, chain
from datetime import datetime, timedelta
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


def generate_requests_time_serie(num_devices, request_period, interval_start, interval_end, resolution):
    """
    Generates a time serie of requests based on some model information.

    :param num_devices: the number of IoT devices.
    :param request_period_in_seconds: the request period in seconds. Indicates how often each device sends requests.
    :param interval_start: the starting date of the interval of the distribution.
    :param interval_end: the ending date of the interval of the distribution.
    :param resolution: the resolution of the time serie in seconds.
    :return: a map function able to materialize a list of tuples with a datetime and the sum of hits from every device (i.e: [('2018-01-01 00:00:01', 23), (, 43)...]).
    """

    # Create device fleet generator (lazy generates a collection of time deltas)
    devices = devices_generator(num_devices, request_period)

    # Create a generator for device periodic requests
    request_period_generator = time_walker(interval_start, request_period, interval_end)

    # Create a "stamper" that fixes deltas into actual datetime stamps for a specific period
    stamper = devices_date_stamper(devices)

    # Create a function that returns the t0 of a period for a given time
    resolution_finder = resolution_period_finder(interval_start, resolution)

    # flatMap = map + reduce
    all_requests = reduce(chain, map(
        stamper, request_period_generator), iter([]))

    requests_by_resolution = map(lambda x: (
        x[0], len(list(x[1]))), groupby(all_requests, resolution_finder))

    return requests_by_resolution


def calculate_costs_by_resolution(resolution, ec2_instances_list, request_time_serie):

    acc_hits = 0

    def calc_ec2_use(ec2_instances_list, num_hits, resolution):
        return tuple(chain([calc_ec2_instance_use(instance, num_hits, resolution) for instance in ec2_instances_list]))

    def calc_ec2_instance_use(ec2_instance, num_hits, resolution):
        num_instances = max(1, ec2_instance.get_num_instances(num_hits/resolution))
        cost = ec2_instance.get_cost(resolution) * num_instances
        return (num_instances, cost)

    def calc_use(row):
        nonlocal acc_hits
        num_hits = row[1]
        acc_hits = acc_hits + num_hits
        ec2_costs = calc_ec2_use(ec2_instances_list, num_hits, resolution)
        return (row[0], num_hits, acc_hits) + ec2_costs

    return map(calc_use, request_time_serie)

def aggregate_costs(lambda_instance, ec2_instances_list, costs_time_serie):

    costs = {'length':0, 'hits':0, 'lambda':0}

    for idx in range(len(ec2_instances_list)):
        costs.update({f'ec2_{idx}_cost':0, f'ec2_{idx}_instances':0})

    def acc(costs, row):
        costs['length'] = costs['length'] + 1
        costs['hits'] = costs['hits'] + row[1]
        for idx in range(len(ec2_instances_list)):
            costs[f'ec2_{idx}_cost'] = costs[f'ec2_{idx}_cost'] + row[3+idx][1]
            costs[f'ec2_{idx}_instances'] = max(costs[f'ec2_{idx}_instances'], row[3+idx][0])
        return costs

    aggregated = reduce(acc, costs_time_serie, costs)
    aggregated['lambda'] = lambda_instance.get_cost(aggregated['hits'], reset_free_tier=True)
    return aggregated

def build_interval(num_days):
    today = datetime.today()
    interval_start = datetime(today.year, 1, 1)
    interval_end = interval_start + timedelta(days=num_days)
    return (interval_start, interval_end)

def main():

    ec2_flavors = ('t2.large', 'm4.large', 'm4.4xlarge')
    req_period_list = [3600, 8* 3600, 24 * 3600]
    num_devices_list = [10, 100, 1000, 10000, 100000,
                        1000000, 10000000, 100000000, 1000000000, 10000000000]
    resolution_in_seconds = 60
    num_days = 30
    lambda_memory = 128
    lambda_request_duration_ms = 200
    interval_start, interval_end = build_interval(num_days)
    ec2_instances = [awscosts.EC2(flavor, MB_per_req=lambda_memory, ms_per_req=lambda_request_duration_ms) for flavor in ec2_flavors]

    print("len, hits, lambda, ec2, resolution, instance_count")

    for req_period in req_period_list:
        for num_devices in num_devices_list:
            lambda_instance = awscosts.Lambda(lambda_memory, lambda_request_duration_ms)
            requests_time_serie = generate_requests_time_serie(num_devices, req_period, interval_start, interval_end, resolution_in_seconds)
            costs_time_serie = calculate_costs_by_resolution(resolution_in_seconds, ec2_instances, requests_time_serie)
            print(aggregate_costs(lambda_instance, ec2_instances, costs_time_serie))

if __name__ == "__main__":
    main()
