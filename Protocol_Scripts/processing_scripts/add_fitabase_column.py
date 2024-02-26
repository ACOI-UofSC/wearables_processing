#!/usr/bin/env python3

import csv
import datetime
import pandas as pd


def gen_file_fitabase_column_agg(agg_file, hr_file):
    """
    This method read data from 'agg_file' and 'hr_file' and put the heart rate
    reading from 'hr_file' as an extra column to the 'agg_file'.

    The output is a new file 'res_file' which combines 'agg_file' and the extra
    column. The 'agg_file' and 'hr_file' remain intact.
    """

    col_name = "Fitabase_HR"

    # load file into DataFrame
    ag = pd.read_csv(agg_file)

    # add an extra column "Fitabase_HR" with empty values
    ag[col_name] = [""] * len(ag)

    hr = pd.read_csv(hr_file)

    # total number of rows for 'agg_file'
    ag_total = len(ag)

    # total number of rows for 'hr_file'
    hr_total = len(hr)

    ag_cnt, hr_cnt = 0, 0

    while (ag_cnt < ag_total) and (hr_cnt < hr_total):

        ag_timestamp = datetime.datetime.strptime(ag["Time"][ag_cnt], '%Y-%m-%d %H:%M:%S')
        hr_timestamp = datetime.datetime.strptime(hr["Time"][hr_cnt], '%m/%d/%Y %I:%M:%S %p')

        if (ag_timestamp < hr_timestamp):
            ag_cnt += 1
        elif (ag_timestamp > hr_timestamp):
            hr_cnt += 1
        else:
            # ag_timestamp == hr_timestamp
            # Since the timestamps are at second-level resolution, we can do this comparison.
            # Otherwise, this should be modified to match the closest timestamps.

            ag.at[ag_cnt, col_name] = int(hr["Value"][hr_cnt])
            ag_cnt += 1
            hr_cnt += 1

    ag.to_csv(agg_file)





def gen_file_fitabase_column_aligned(aligned_file, hr_file):
    """
    This method read data from 'aligned_file' and 'hr_file' and put the heart rate
    reading from 'hr_file' as an extra column to the 'aligned_file'.


    """

    col_name = "Fitabase_HR"

    # load file into DataFrame
    al = pd.read_csv(aligned_file)

    # add an extra column "Fitabase_HR" with empty values
    al[col_name] = [""] * len(al)

    hr = pd.read_csv(hr_file)

    # total number of rows for 'agg_file'
    al_total = len(al)

    # total number of rows for 'hr_file'
    hr_total = len(hr)

    al_cnt, hr_cnt = 0, 0

    while (al_cnt < al_total) and (hr_cnt < hr_total):
        try:
            actigraph_time = al["Actigraph Time"][al_cnt]
        except:
            actigraph_time = al["Axivity Time"][al_cnt]
        al_timestamp = datetime.datetime.strptime(actigraph_time[:-4], '%Y-%m-%d %H:%M:%S')
        hr_timestamp = datetime.datetime.strptime(hr["Time"][hr_cnt], '%m/%d/%Y %I:%M:%S %p')

        if (al_timestamp < hr_timestamp):
            al_cnt += 1
        elif (al_timestamp > hr_timestamp):
            hr_cnt += 1
        else:
            # ag_timestamp == hr_timestamp
            # Since the timestamps are at second-level resolution, we can do this comparison.
            # Otherwise, this should be modified to match the closest timestamps.

            al.at[al_cnt, col_name] = int(hr["Value"][hr_cnt])
            al_cnt += 1
            hr_cnt += 1

    try:
        al.to_csv(aligned_file)
    except:pass