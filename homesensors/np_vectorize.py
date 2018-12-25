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
from datetime import datetime
#%%
df = pd.read_csv("balcony_temperature.csv")
print(f"dtypes:")
print(df.dtypes)
print(f"shape   : {df.shape}")
print("head:")
print(df.head())
v = np.vectorize(timestamp_to_day)
df["day"] = v(df['time'])
df.head()
