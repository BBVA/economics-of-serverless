import webish_simulator as ws
import pandas as pd
import datetime
import numpy


def test_simulator():
    startdate = datetime.datetime.now()
    dataframe = pd.DataFrame(
        numpy.random.randn(31),
        index=pd.date_range(start=startdate, periods=24, freq='H'),
        columns=['date', 'hits']
    )
    print(dataframe.head())
    ws.simulate(dataframe)
