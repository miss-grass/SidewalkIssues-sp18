

# Scatterplot Matrix
import matplotlib.pyplot as plt
import pandas
from pandas.plotting import scatter_matrix
url = "/Users/Miss-grass/Documents/CSE495/Sp18/routeStat_only3.csv"
names = ['std_dev', 'skewness', 'kurtosis']
data = pandas.read_csv(url, names=names)
scatter_matrix(data)
plt.show()
