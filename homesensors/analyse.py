#%% [markdown]
# ## Run preprocessor.py manually
# in all other cases add 'from preprocess import csv_2_days'
#%%
from preprocess import *
#%%
import numpy as np
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
