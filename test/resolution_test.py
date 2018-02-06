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

from datetime import datetime
from iot.simulator import resolution_period_finder


def test_resolution_period_smaller():
    start = datetime(2017, 1, 1, 12, 0)
    period_0 = datetime(2017, 1, 1, 12, 29)
    period_1 = datetime(2017, 1, 1, 12, 31)
    period_2 = datetime(2017, 1, 1, 13, 0)
    period_3 = datetime(2017, 1, 1, 13, 59)

    finder = resolution_period_finder(start, 1800)
    assert finder(period_0) == datetime(2017, 1, 1, 12, 0)
    assert finder(period_1) == datetime(2017, 1, 1, 12, 30)
    assert finder(period_2) == datetime(2017, 1, 1, 13, 0)
    assert finder(period_3) == datetime(2017, 1, 1, 13, 30)


def test_resolution_period_bigger():
    start = datetime(2017, 1, 1, 12, 0)
    period_0 = datetime(2017, 1, 1, 13, 29)
    period_1 = datetime(2017, 1, 1, 15, 31)
    period_2 = datetime(2017, 1, 1, 16, 10)
    period_3 = datetime(2017, 1, 1, 18, 9)

    finder = resolution_period_finder(start, 3600*2)
    assert finder(period_0) == datetime(2017, 1, 1, 12, 0)
    assert finder(period_1) == datetime(2017, 1, 1, 14, 0)
    assert finder(period_2) == datetime(2017, 1, 1, 16, 0)
    assert finder(period_3) == datetime(2017, 1, 1, 18, 0)
