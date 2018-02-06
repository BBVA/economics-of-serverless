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

from random import randint
from datetime import datetime, timedelta
from iot.simulator import devices_generator
from iot.simulator import devices_date_stamper
from iot.simulator import devices_growth


def test_devices_generator():
    res = next(devices_generator(10, 60))
    assert len(res) == 10, "10 expected {} obtained".format(len(res))
    assert all(map(lambda x: x < 60, res)), "all must be under 60 seconds"


def test_devices_mapper():
    res = devices_generator(10, 60)
    mapper = devices_date_stamper(res)
    current_date = datetime(2018, 1, 1)
    on_date = list(next(map(mapper, [current_date])))
    assert len(on_date) == 10, "Should not change the number of devices, expected 10, current {}".format(len(on_date))
    max_expected_date = current_date + timedelta(seconds=60)
    assert all(map(lambda x: current_date <= x < max_expected_date, on_date)), "all must be in period"


def test_devices_growth():
    max_delta_in_seconds = 60

    def growth_function(current_devices):
        return current_devices + [randint(0, max_delta_in_seconds-1)]
    devices = devices_generator(10, max_delta_in_seconds)
    to_check = next(devices)
    devices_growth_generator = devices_growth(devices, growth_function)
    assert any(map(lambda x: x not in to_check, devices_growth_generator))
