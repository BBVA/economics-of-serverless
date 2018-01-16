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


def test_simulator(df=dataframe):
    # print(dataframe.head())
    assert type(ws.simulate(df)) == pd.DataFrame


def test_normalization(df=dataframe):
    print(df.head())
    result = ws.simulate(df)
    sum_norm = result['reqs_normalized'].sum()
    assert int(round(sum_norm)) == 1
