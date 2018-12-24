#%%
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
#%%
df = pd.read_csv("C:/Users/wassfila/Projects/balcony_temperature.csv")
plt.ion()

#%%
df.columns.values
df.dtypes
df["temperature"].head()


#%%
#datetime.datetime.utcfromtimestamp(1527326276813117952)
#datetime.date.fromtimestamp(1527326276813117952)
dt = datetime.fromtimestamp(1527326276813117952 // 1000000000)
print(dt.strftime('%Y-%m-%d'))

#%%
d1 = datetime.strptime('2018 05 26', '%Y %m %d')
print(d1.strftime('%Y-%m-%d'))

#%%
def timestamp_to_day(ts):
    dt = datetime.fromtimestamp(ts // 1000000000)
    return dt.strftime('%Y-%m-%d')
#df['days'] = Series(timestamp_to_day(sLength), index=df1.index)