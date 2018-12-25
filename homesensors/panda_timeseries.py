#%% [markdown]
# squeeze(True,False) returns a time series
#
# using date_parser=pd.to_datetime with default units="ns" gets the error of Python int too large to convert to C long
# this is incenvenient because ns is the default influx export, and python code is slow at converting each entry to ms
#
# ## references
# 
#[PythonDataScienceHandbook](https://colab.research.google.com/github/jakevdp/PythonDataScienceHandbook/blob/master/notebooks/03.11-Working-with-Time-Series.ipynb)
#
#[pandas read_csv and epochtime](https://kaijento.github.io/2017/03/29/pandas-read_csv-epoch/)
#
# [read_csv](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.read_csv.html)
# 
# [to_datetime](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.to_datetime.html)
#

#%%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#%%
df = pd.read_csv("balcony_temperature_series.csv", 
                    index_col="time", 
                    squeeze=True ,
                    date_parser=lambda ts:pd.to_datetime(int(ts) // 1000, unit="us")
                )

#%%
print(df.dtypes)
print("--- shape ---")
print(df.shape)
print("--- head ---")
print(df.head())
#%%
#time selection
print(df["2018-06-27":"2018-06-28"].count())
print(df["2018-06-29"].count())
print(df["2018-06-27":"2018-06-27 00:30"])
#%%
df["2018-06-27":"2018-07-10"].plot(figsize=(10,5))
#%%
#plt.rcParams['figure.figsize'] = [200, 100]
#%%
fewdays = df["2018-08-01":"2018-08-3"]
fewdays.plot(alpha=0.5, style='-',figsize=(20,10))
fewdays.resample('2 H').mean().plot(style=':')
fewdays.asfreq('2 H').plot(style='--')
plt.legend(['input', 'resample', 'asfreq'],loc='upper left')

#%%
rolling = fewdays.rolling('2 H')

data = pd.DataFrame({'input': fewdays,
                     'few days rolling_mean': rolling.mean()})
ax = data.plot(style=['-', '--'], figsize=(20,10))
ax.lines[0].set_alpha(0.3)
#%%
#rolling = fewdays.rolling(20, center=True)
rolling = fewdays.rolling('2 H')

data = pd.DataFrame({'input': fewdays,
                     'few days rolling_mean': rolling.mean(),
                     'few days rolling_std': rolling.std()})
ax = data.plot(style=['-', '--', ':'], figsize=(20,10))
ax.lines[0].set_alpha(0.3)
