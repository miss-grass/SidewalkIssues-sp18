import numpy as np
import pandas as pd
from numpy import math
import matplotlib.pyplot as plt
import scipy as sp
from scipy import stats


def main():
    trips = pd.read_csv('/Users/Miss-grass/Documents/CSE495/Sp18/data/api_transfer/transfer_clean.csv', skipinitialspace=True, dtype=object)
    # initial id
    id_p = 1
    exit_lat_p = '47.1667'
    exit_lon_p = '-122.517'
    transfer_stop_lat_p = '47.1653'
    transfer_stop_lon_p = '-122.512'

    df = pd.DataFrame(columns=['route number',
                               'start location (GPS)',
                               'end location (GPS)',
                               'AccessMap recommended route',
                               'distance by AccessMap',
                               'minor issue number',
                               'severe issue number',
                               'time distribution (a delimited list of all the times)',
                               'mean time',
                               'std dev time',
                               'median time',
                               'skewness time',
                               'kurtosis time'])
    time = []

    for index, row in trips.iterrows():
        id = row['api_transfer_id']
        if id is np.NaN:
            # add last row into df
            df.loc[df.shape[0]] = [id_p,
                                   exit_lat_p + "," + exit_lon_p,
                                   transfer_stop_lat_p + "," + transfer_stop_lon_p,
                                   None,
                                   None,
                                   None,
                                   None,
                                   time,
                                   np.mean(time),
                                   np.std(time),
                                   np.median(time),
                                   stats.skew(time),
                                   stats.kurtosis(time)]
            print(id_p)
            break
        id = int(id)
        exit_lat = row['exit_lat']
        exit_lon = row['exit_lon']
        transfer_stop_lat = row['transfer_stop_lat']
        transfer_stop_lon = row['transfer_stop_lon']
        if id != id_p:
            # add row into df
            df.loc[df.shape[0]] = [id_p,
                                   exit_lat_p + "," + exit_lon_p,
                                   transfer_stop_lat_p + "," + transfer_stop_lon_p,
                                   None,
                                   None,
                                   None,
                                   None,
                                   time,
                                   np.mean(time),
                                   np.std(time),
                                   np.median(time),
                                   stats.skew(time),
                                   stats.kurtosis(time)]

            print(id_p)
            # reinitialize each variable
            id_p = id
            exit_lat_p = exit_lat
            exit_lon_p = exit_lon
            transfer_stop_lat_p = transfer_stop_lat
            transfer_stop_lon_p = transfer_stop_lon
            time = []

        time.append(int(row['transfer_duration_seconds']))

    filename = "/Users/Miss-grass/Documents/CSE495/Sp18/output/routeStat.csv"
    df.to_csv(filename,  encoding='utf-8')



if __name__ == "__main__":
    main()

