#%%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("balcony_temperature_series.csv", 
                    index_col="time", 
                    squeeze=True ,
                    date_parser=lambda ts:pd.to_datetime(int(ts) // 1000, unit="us")
                )
#%%
fewdays = df["2018-05-27":"2018-08-31"]
fewdays.resample('D').count().plot()
#%%
df.resample('D').count().hist()
