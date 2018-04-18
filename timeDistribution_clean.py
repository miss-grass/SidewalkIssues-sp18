import numpy as np
import pandas as pd
from numpy import math
import matplotlib.pyplot as plt



def main():
    trips = pd.read_csv('/Users/Miss-grass/Documents/CSE495/Sp18/data/api_transfer/transfer_clean.csv', skipinitialspace=True, dtype=object)
    # initial id
    id_p = 1

    time = []
    for index, row in trips.iterrows():
        id = row['api_transfer_id']
        if id is None:
            break
        else:
            id = int(id)
        if id != id_p:
            # plot distribution
            plt.xlabel('transfer duration seconds')
            plt.ylabel('frequency')
            plt.hist(time, bins=100)  # arguments are passed to np.histogram
            title = "Time distribution of route " + str(id_p)
            plt.title(title)
            savepath = "Sp18/output/distribution_clean/" + str(id_p)
            plt.savefig(savepath)
            print("saved to " + savepath)
            plt.close()

            # reinitialize each variable
            id_p = id
            time = []

        time.append(int(row['transfer_duration_seconds']))

    # plot last distribution
    plt.xlabel('transfer duration seconds')
    plt.ylabel('frequency')
    plt.hist(time, bins=100)  # arguments are passed to np.histogram
    title = "Time distribution of route " + str(id_p)
    plt.title(title)
    savepath = "Sp18/output/distribution_clean/" + str(id_p)
    plt.savefig(savepath)
    print("saved to " + savepath)
    plt.close()



if __name__ == "__main__":
    main()

