from iot.simulator import time_walker
from datetime import datetime


def test_time_walker():
    start = datetime(2017, 1, 1)
    end = datetime(2017, 1, 2)
    res = list(time_walker(start, 3600, end))

    assert len(res) == 24, "must walk 24h"
    assert all(map(lambda x: start <= x <= end, res)), "all must fit in day"
