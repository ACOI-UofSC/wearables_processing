import pandas as pd
from datetime import datetime
from .data_summary import calc_enmo

def time_convert(a_time):
    return datetime.strptime(a_time, '%Y-%m-%d %H:%M:%S.%f')

def process_axivity(data_paths, start, end) :
    # Read in file and store it as a dataframe.

    axivity_data = pd.read_csv(data_paths[0], skiprows=0, names=["Time", "X", "Y", "Z"], parse_dates=['Time'],
                               date_parser=time_convert)

    axivity_data = axivity_data.loc[(axivity_data['Time'] >= start) & (axivity_data['Time'] <= end), :]
    sec_frac = axivity_data["Time"].apply(lambda x: x.microsecond)
    axivity_data.insert(1, 'Second Fraction', sec_frac)
    mag, enmo = calc_enmo(axivity_data.loc[:, ['X', 'Y', 'Z']])
    axivity_data.insert(5, "Magnitude", mag)
    axivity_data.insert(6, "ENMO", enmo)
    return ["Axivity", axivity_data]