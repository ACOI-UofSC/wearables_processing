#!/usr/bin/env python

import datetime as dt

import sys
if __name__=='__main__':
    if len(sys.argv) != 2:
        print("usage: python", sys.argv[0], "<time string: yyyy-mm-dd_HH:MM:SS.f>")
        sys.exit(1)

    tstr = sys.argv[1]
    dtime = dt.datetime.strptime(tstr, '%Y-%m-%d_%H:%M:%S.%f')
    print(dtime.timestamp()*1000)
    
