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

import awscosts
import pytest


def test_no_params():
    with pytest.raises(ValueError):
        awscosts.EC2("t2.micro")

    with pytest.raises(ValueError):
        awscosts.EC2("t2.micro", ms_per_req=200)

    with pytest.raises(ValueError):
        awscosts.EC2("t2.micro", MB_per_req=200)


def test_init_1():
    t2micro = awscosts.EC2('t2.micro', max_reqs_per_second=200)
    assert t2micro.max_reqs_per_second == 200


def test_max_reqs():
    t2micro = awscosts.EC2('t2.micro', ms_per_req=200, MB_per_req=1024)
    assert t2micro.max_reqs_per_second == 5


def test_scalability():
    max_reqs = 200
    t2micro = awscosts.EC2('t2.micro', max_reqs_per_second=max_reqs)
    assert t2micro.get_num_instances(max_reqs + 1) == 2
