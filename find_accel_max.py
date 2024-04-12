#!/usr/bin/env python

#import math

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import datetime as dt


ACCEL_COL_NAMES = ["LocalTime", "Timestamp", "x", "y", "z"]
TIME_STR = "%Y-%m-%d_%H:%M:%S"

def find_max_accel(filename, start_time, end_time):
    df = pd.read_csv(filename, header=None, names=ACCEL_COL_NAMES)
    #print(df)
    df["Norm"] = np.sqrt(df["x"]**2 + df["y"]**2 + df["z"]**2)
    df["Time"] = df['Timestamp'].apply(lambda x: dt.datetime.fromtimestamp(x/1000))

    tstart = dt.datetime.strptime(start_time, TIME_STR)
    tend = dt.datetime.strptime(end_time, TIME_STR)

    # Filter the DataFrame
    filtered_df = df[(df['Time'] >= tstart) & (df['Time'] <= tend)]

    # Find the row with the maximum 'Norm' value
    max_norm_row = filtered_df[filtered_df['Norm'] == filtered_df['Norm'].max()]

    return max_norm_row


import sys

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("usage: python", sys.argv[0], "<accel_file> <start_time yyyy-mm-dd_HH:MM:SS> <end_time yyyy-mm-dd_HH:MM:SS>")
        sys.exit(1)

    filename = sys.argv[1]
    start_time = sys.argv[2]
    end_time = sys.argv[3]
    
    rec = find_max_accel(filename, start_time, end_time)
    print(rec)
