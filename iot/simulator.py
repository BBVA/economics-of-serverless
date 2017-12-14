from functools import reduce
from itertools import chain, groupby
from random import randint
from datetime import timedelta
from datetime import datetime

import math


def time_walker(start: datetime, delta_in_seconds: int, end: datetime):
    """
    From starting point, and delta, will generate all dates between until end.

    :param start:
    :param delta_in_seconds:
    :param end:
    :return:
    """
    while start < end:
        yield start
        start += timedelta(seconds=delta_in_seconds)


def devices_generator(number_of_devices: int, max_delta_in_seconds: int):
    """
    Must generate the devices parking represented by their time delta from start period window.
    It will return constantly the same numbers at infinite.

    :param number_of_devices:
    :param max_delta_in_seconds:
    :return:
    """
    devices = sorted([randint(0, max_delta_in_seconds-1) for _ in range(0, number_of_devices)])
    while True:
        yield devices


def devices_growth(devices, growth_function):
    """
    generator, every time you call will growth

    :param devices:
    :param growth_function:
    :return:
    """
    devices = next(devices)
    i = len(devices)
    while True:
        yield devices
        (devices, i) = growth_function(devices, i)
        devices = sorted(devices)


def devices_date_stamper(devices):
    """
    Return a function that given a date time will return the dates when devices will make their requests.

    :param devices:
    :return:
    """
    def mapper(date):
        def stamper(x):
            return date + timedelta(seconds=x)
        return map(stamper, next(devices))
    return mapper


def resolution_period_finder(start: datetime, resolution_period_in_seconds: int):
    """
    Return a function that given any date will give you the resolution period in datetime.

    :return:
    """
    delta = timedelta(seconds=resolution_period_in_seconds)

    def period(date: datetime):
        if date >= start:
            diff = date - start
            n = math.floor(diff.seconds / resolution_period_in_seconds)
            return start + timedelta(days=diff.days) + (delta * n)
        else:
            return None
    return period


if __name__ == '__main__':
    request_period_in_seconds = 3600 * 12
    start = datetime(2017, 1, 1)
    end = datetime(2017, 12, 31)
    resolution_period = 60

    devices = devices_generator(100, request_period_in_seconds)
    request_period_generator = time_walker(start, request_period_in_seconds, end)
    resolution_finder = resolution_period_finder(start, resolution_period)


    def growth_function(current_devices, i):
        ni = int(math.floor(i * 0.01))
        return current_devices + [randint(0, request_period_in_seconds - 1) for _ in range(0, ni)], i + ni


    devices_growth_generator = devices_growth(devices, growth_function)
    stamper = devices_date_stamper(devices_growth_generator)

    # flatMap = map + reduce
    all_request = reduce(chain, map(stamper, request_period_generator), iter([]))
    for period, res in groupby(all_request, resolution_finder):
        actual = list(res)
        print("p:{}, l: {}, d:{}".format(period, len(actual), actual))
