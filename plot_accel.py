#!/usr/bin/env python

#import math

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import datetime as dt


ACCEL_COL_NAMES = ["LocalTime", "Timestamp", "x", "y", "z"]

def plot_accel(filename):
    df = pd.read_csv(filename, header=None, names=ACCEL_COL_NAMES)
    #print(df)
    df["Norm"] = np.sqrt(df["x"]**2 + df["y"]**2 + df["z"]**2)
    df["Time"] = df['Timestamp'].apply(lambda x: dt.datetime.fromtimestamp(x/1000))

    plt.figure(figsize=(10,6))
    plt.plot(df["Time"], df["Norm"], label="Accel")
    plt.ylabel("Norm")
    plt.xlabel("Time")
    plt.show()
    

import sys

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("usage: python", sys.argv[0], "<accel_file>")
        sys.exit(1)

    filename = sys.argv[1]
    plot_accel(filename)
