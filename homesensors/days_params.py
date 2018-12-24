#%%
import os
import sys
nb_dir = os.path.split(os.getcwd())[0]
if nb_dir not in sys.path:
    sys.path.append(nb_dir)
from homesensors.preprocess import *

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#%%
filename = "../balcony_temperature.csv"
days = csv_2_days(filename)
print(f"loaded {len(days)} days")
#%%
plt.plot(days["2018-05-28"]["timestamp"], days["2018-05-28"]["temperature"])
plt.show()
#%%
days_add_params(days)
print(f'average = {days["2018-05-28"]["mean"]}')
#%%
a = days["2018-05-28"]["temperature"]
plt.hist(a, bins='auto')  # arguments are passed to np.histogram
plt.title("Histogram with 'auto' bins")
plt.show()

#%%
series = days_to_array(days)
df = pd.DataFrame(series)
df.plot('day', 'min')
plt.show()

#%%
plt.plot( 'day', 'min', data=df, marker='',  color='skyblue', linewidth=2)
plt.plot( 'day', 'mean', data=df, marker='', color='olive', linewidth=4)
plt.plot( 'day', 'max', data=df, marker='', color='red', linewidth=2)
plt.show()
