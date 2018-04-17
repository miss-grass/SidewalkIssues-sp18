import numpy as np
import pandas as pd
from numpy import math



def main():
    trips = pd.read_csv('data/transfer_trips_/transfer_trips.csv', skipinitialspace=True, dtype=object)
    # initial route
    ei_p = 9
    ep_p = 6
    ti_p = 9
    tp_p = 6
    df = pd.DataFrame(columns=['original row',
                               'transfer_duration_seconds',
                               'num_passengers',
                               'first_service_provider',
                               'exit_stop_id',
                               'exit_lat',
                               'exit_lon',
                               'transfer_newservice_provider',
                               'transfer_boarding_stop_id',
                               'transfer_stop_lat',
                               'transfer_stop_lon'])
    dest = "output/tripPerRoute/"
    for _, row in trips.iterrows():
        ei = int(row['exit_stop_id'])
        ep = int(row['first_service_provider'])
        ti = int(row['transfer_boarding_stop_id'])
        tp = int(row['transfer_newservice_provider'])
        if ei != ei_p or ep != ep_p or ti != ti_p or tp != tp_p:
            # output df so far
            filename = dest + str(ei_p) + "-" + str(ep_p) + "-to-" + str(ti_p) + "-" + str(tp_p) + ".csv"
            df.to_csv(filename, sep=',', encoding='utf-8')

            # reinitialize each variable
            ei_p = ei
            ep_p = ep
            ti_p = ti
            tp_p = tp
            df = pd.DataFrame(columns=['original row',
                                       'transfer_duration_seconds',
                                       'num_passengers',
                                       'first_service_provider',
                                       'exit_stop_id',
                                       'exit_lat',
                                       'exit_lon',
                                       'transfer_newservice_provider',
                                       'transfer_boarding_stop_id',
                                       'transfer_stop_lat',
                                       'transfer_stop_lon'])

        df.loc[len(df)] = [row['row number'],
                               row['transfer_duration_seconds'],
                               row['num_passengers'],
                               ep, ei,
                               row['exit_lat'],
                               row['exit_lon'],
                               tp, ti,
                               row['transfer_stop_lat'],
                               row['transfer_stop_lon']]




if __name__ == "__main__":
    main()

