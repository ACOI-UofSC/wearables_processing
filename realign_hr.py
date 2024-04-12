#!/usr/bin/env python

#import math

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import datetime as dt


HR_COL_NAMES = ["LocalTime", "Timestamp", "hr"]

def realign_accel(filename, diff):
    df = pd.read_csv(filename, header=None, names=HR_COL_NAMES)
    #print(df)

    df["Timestamp"] += diff

    df.to_csv('realigned.csv', header=False, index=False)
    

import sys

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("usage: python", sys.argv[0], "<hr_file> <from_timestamp> <to_timestamp>")
        sys.exit(1)

    filename = sys.argv[1]
    ts_from = sys.argv[2]
    ts_to = sys.argv[3]

    diff = int(ts_to) - int(ts_from)
    
    realign_accel(filename, diff)
