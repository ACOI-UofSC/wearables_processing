#!/usr/bin/env python

def process(filename, freq):
    gap = 1000 // freq
    flag = True

    with open(filename, 'r') as f:
        line = f.readline()
        line = line.strip()
        tokens = line.split(",")

        target_ts = int(tokens[1])
        ts_diff = 9999999999999
        min_record = None

        while line:
            line = line.strip()
            tokens = line.split(',')
            ts = int(tokens[1])
            
            if abs(target_ts - ts) > ts_diff:
                print(min_record)
                target_ts = min_ts + gap
            
            min_ts = ts
            min_record = line

            ts_diff = abs(target_ts - ts)

            line = f.readline()


    

import sys
if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python ", sys.argv[0], "<filename> <target_freq>")
        sys.exit(1)

    filename = sys.argv[1]
    freq = int(sys.argv[2])
    
    process(filename, freq)
