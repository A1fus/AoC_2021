import pandas as pd


"""count the number of times a depth measurement increases from the previous measurement."""

data = pd.read_csv("input/day1.csv", header=None, usecols=[0])
data_diff = data.diff()
data_diff = data_diff[data_diff[0] > 0]
print(data_diff.count())
