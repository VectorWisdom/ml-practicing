#%%
from datetime import datetime
import numpy as np

def timestamp_to_day(ts):
    dt = datetime.fromtimestamp(ts // 1000000000)
    return dt.strftime('%Y-%m-%d')

def csv_2_days_map(filename):
    nb_lines = 0
    days = {}
    with open(filename) as f:
        for i,line in enumerate(f):
            if(i == 0):
                header = line.replace('\n','').split(',')
                print(f"header: {header}")
            else:
                nb_lines = nb_lines + 1
                entries = line.split(',')
                day_name = timestamp_to_day(int(entries[1]))
                if(not day_name in days):
                    days[day_name] = {}
                    days[day_name]["timestamp"] = []
                    days[day_name]["temperature"] = []
                days[day_name]["timestamp"].append(entries[1])
                days[day_name]["temperature"].append(entries[2])
    return days

def csv_2_days_np(filename):
    days = csv_2_days_map(filename)
    np_days = {}
    for day in days:
        np_days[day] = {}
        np_days[day]["timestamp"] = np.array(days[day]["timestamp"]).astype("datetime64")
        np_days[day]["temperature"] = np.array(days[day]["temperature"]).astype("float")
    return np_days



def days_add_params(days):
    for day in days:
        days[day]["mean"] = np.mean(days[day]["temperature"])
    return