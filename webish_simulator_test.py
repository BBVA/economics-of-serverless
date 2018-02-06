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

import webish_simulator as ws
import pandas as pd
import datetime
import numpy


weeks = 4
total_hours = weeks * 24 * 7
startdate = datetime.datetime.now()
dataframe = pd.DataFrame(
    numpy.random.randint(100, total_hours),
    index=pd.date_range(start=startdate, periods=total_hours, freq='H'),
    columns=('hits',)
)

monthly_hits = 28 * 24
output_df = ws.simulate(dataframe, monthly_scale_factor=monthly_hits)


def test_simulator(df=output_df):
    # print(dataframe.head())
    assert type(df) == pd.DataFrame


def test_normalization(df=output_df):
    sum_norm = df['reqs_normalized'].sum()
    assert int(round(sum_norm)) == 1


def test_scale_factor(df=output_df):
    assert df['requests'].sum() == monthly_hits


def test_costs(df=output_df):
    output_df = ws.get_cost(df)
    assert type(output_df) == pd.DataFrame
