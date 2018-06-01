import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from sklearn.cluster import KMeans

#np.random.seed(5)


d = pd.DataFrame(columns=['route number',
                          'start location (GPS)',
                          'end location (GPS)',
                          'accessmap recommended path',
                          'distance by AccessMap',
                          'minor issue',
                          'severe issue',
                          'time distribution (a delimited list of all the times)',
                          'mean time',
                          'std dev time',
                          'median time',
                          'skewness time',
                          'kurtosis time'])
df = pd.read_csv('/Users/Miss-grass/Documents/CSE495/Sp18/output/routeStat.csv', skipinitialspace=True, dtype=object)
df = df[df['distance by AccessMap'] != '0']
df = df[df['accessmap recommended path'] != '0']

for index, row in df.iterrows():
    if len(row['time distribution (a delimited list of all the times)'].split(',')) >= 5:
        d.loc[d.shape[0]] = row
print(d.shape)
filename = "filteredRoute.csv"
d.to_csv(filename, sep=',', encoding='utf-8')