#%%
import os
import sys
nb_dir = os.path.split(os.getcwd())[0]
if nb_dir not in sys.path:
    sys.path.append(nb_dir)
import homesensors.preprocess as prep

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
#%%
df = pd.read_csv("balcony_temperature.csv")
print(f"dtypes:")
print(df.dtypes)
print(f"shape   : {df.shape}")
print("head:")
print(df.head())
v = np.vectorize(prep.timestamp_to_day)
df["day"] = v(df['time'])
df.head()

#%%
df2 = df.copy()
grouped = df2.groupby(by="day")
agg = grouped["temperature"].agg([np.sum, np.mean, np.std])
print("--- aggregate ---")
print(agg.head())
#%%
someday = grouped.get_group("2018-05-29")
plt.plot( 'time', 'temperature', data=someday, marker='', color='blue', linewidth=1)
plt.show()
print(someday.head())
