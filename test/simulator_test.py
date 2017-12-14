from datetime import datetime
from functools import reduce
from itertools import groupby, chain
from random import randint

import math

from iot.simulator import devices_generator, time_walker, resolution_period_finder, devices_date_stamper, devices_growth


def test_simulator_no_growth():
    request_period_in_seconds = 60
    start = datetime(2017, 1, 1)
    end = datetime(2017, 1, 2)
    resolution_period = 3600

    devices = devices_generator(10, request_period_in_seconds)
    request_period_generator = time_walker(start, request_period_in_seconds, end)
    resolution_finder = resolution_period_finder(start, resolution_period)

    stamper = devices_date_stamper(devices)
    # flatMap = map + reduce
    all_request = reduce(chain, map(stamper, request_period_generator), iter([]))
    for _, res in groupby(all_request, resolution_finder):
        assert len(list(res)) == 600


def test_simulator_growth():
    request_period_in_seconds = 60
    start = datetime(2017, 1, 1)
    end = datetime(2017, 1, 2)
    resolution_period = 1

    devices = devices_generator(10, request_period_in_seconds)
    request_period_generator = time_walker(start, request_period_in_seconds, end)
    resolution_finder = resolution_period_finder(start, resolution_period)

    def growth_function(current_devices, i):
        return current_devices + [randint(0, request_period_in_seconds-1)], i+1

    devices_growth_generator = devices_growth(devices, growth_function)
    stamper = devices_date_stamper(devices_growth_generator)

    # flatMap = map + reduce
    all_request = reduce(chain, map(stamper, request_period_generator), iter([]))
    for period, res in groupby(all_request, resolution_finder):
        actual = list(res)
        # print(period, len(actual))
        assert actual


def test_simulator_growth_max_by_minute():
    request_period_in_seconds = 60
    start = datetime(2017, 1, 1)
    end = datetime(2017, 1, 2)
    resolution_period = 1

    devices = devices_generator(10, request_period_in_seconds)
    request_period_generator = time_walker(start, request_period_in_seconds, end)
    resolution_finder = resolution_period_finder(start, resolution_period)
    minute_resolution = resolution_period_finder(start, 60)

    def growth_function(current_devices, i):
        return current_devices + [randint(0, request_period_in_seconds-1)], i+1

    devices_growth_generator = devices_growth(devices, growth_function)
    stamper = devices_date_stamper(devices_growth_generator)

    # flatMap = map + reduce
    all_request = reduce(chain, map(stamper, request_period_generator), iter([]))
    by_min = groupby(map(lambda x: (x[0], len(list(x[1]))), groupby(all_request, resolution_finder)),
                     lambda k: minute_resolution(k[0])
                     )
    for minute, reqs in by_min:
        print(minute)
        print(max(map(lambda x: x[1], reqs)))
