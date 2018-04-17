import numpy as np
import pandas as pd
from numpy import math
import glob
import matplotlib.pyplot as plt


def main():
    path = "output/tripPerRoute"
    allFiles = glob.glob(path + "/*.csv")

    for file_ in allFiles:
        print("processing " + file_)
        df = pd.read_csv(file_, index_col=None, header=0)
        list = []
        for _,row in df.iterrows():
            list.append(int(row['transfer_duration_seconds']))
        #bins = np.arange(1, 25)
        print(list)
        plt.xlabel('transfer duration seconds')
        plt.ylabel('frequency')
        plt.hist(list)  # arguments are passed to np.histogram
        savename = file_.split(".")[0].split("/")[2]
        title = "Time distribution of route " + savename
        plt.title(title)
        savepath = "output/distribution/" + savename
        plt.savefig(savepath)
        print("saved to " + savepath)
        plt.close()



if __name__ == "__main__":
    main()

