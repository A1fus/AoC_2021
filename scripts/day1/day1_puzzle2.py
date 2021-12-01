import pandas as pd


"""Start by comparing the first and second three-measurement windows. The measurements in the first window are marked A
(199, 200, 208); their sum is 199 + 200 + 208 = 607. The second window is marked B (200, 208, 210); its sum is 618.
The sum of measurements in the second window is larger than the sum of the first, so this first comparison increased.

Your goal now is to count the number of times the sum of measurements in this sliding window increases from the previous
sum. So, compare A with B, then compare B with C, then C with D, and so on. Stop when there aren't enough measurements
left to create a new three-measurement sum.
"""

data = pd.read_csv("input/day1.csv", header=None, usecols=[0])
data = data.rename({0: "depth"}, axis="columns")
data = data.rolling(3, center=True).sum()

data_diff = data.diff()
data_diff = data_diff[data_diff["depth"] > 0]
print(data_diff.count())
