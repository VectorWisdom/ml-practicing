#%% [markdown]
# ## Run preprocessor.py manually
# in all other cases add 'from preprocess import csv_2_days'
#%%
from preprocess import *
#%%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

filename = "C:/Users/wassfila/Projects/balcony_temperature.csv"
days = csv_2_days_map(filename)
print(f"nb days loaded = {len(days)}")

#%%
np_time = np.array(days["2018-05-27"]["timestamp"]).astype("datetime64")
np_temp = np.array(days["2018-05-27"]["temperature"]).astype("float")

plt.plot(np_time, np_temp)
plt.show()
#%%
np_days = csv_2_days_np(filename)
plt.plot(np_days["2018-05-28"]["timestamp"], np_days["2018-05-28"]["temperature"])
plt.show()
#%%
days_add_params(np_days)
print(f'average = {np_days["2018-05-28"]["mean"]}')
#%%
a = np_days["2018-05-28"]["temperature"]
plt.hist(a, bins='auto')  # arguments are passed to np.histogram
plt.title("Histogram with 'auto' bins")
plt.show()

#%%
series = days_to_array(np_days)

plt.plot(series["min"])
plt.show()

#%%
df = pd.DataFrame(  {   
                        't':series["day"], 
                        'mean':series["mean"],
                        'min':series["min"],
                        'max':series["max"]
                    })
df.plot('t', 'min')
plt.show()

#%%
plt.plot( 't', 'min', data=df, marker='',  color='skyblue', linewidth=2)
plt.plot( 't', 'mean', data=df, marker='', color='olive', linewidth=4)
plt.plot( 't', 'max', data=df, marker='', color='red', linewidth=2)
plt.show()
