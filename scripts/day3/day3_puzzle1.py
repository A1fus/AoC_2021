import pandas as pd
from numpy import *


"""You need to use the binary numbers in the diagnostic report to generate two new binary numbers (called the gamma 
rate and the epsilon rate). The power consumption can then be found by multiplying the gamma rate by the epsilon rate.

Each bit in the gamma rate can be determined by finding the most common bit in the corresponding position of all 
numbers in the diagnostic report. For example, given the following diagnostic report:

00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010

Considering only the first bit of each number, there are five 0 bits and seven 1 bits. Since the most common bit is 1, 
the first bit of the gamma rate is 1.

The most common second bit of the numbers in the diagnostic report is 0, so the second bit of the gamma rate is 0.

The most common value of the third, fourth, and fifth bits are 1, 1, and 0, respectively, and so the final three bits 
of the gamma rate are 110.

So, the gamma rate is the binary number 10110, or 22 in decimal.

The epsilon rate is calculated in a similar way; rather than use the most common bit, the least common bit from each 
position is used. So, the epsilon rate is 01001, or 9 in decimal. Multiplying the gamma rate (22) by the epsilon rate 
(9) produces the power consumption, 198.

Use the binary numbers in your diagnostic report to calculate the gamma rate and epsilon rate, then multiply them 
together. What is the power consumption of the submarine? (Be sure to represent your answer in decimal, not binary.)"""

data = pd.read_csv("input/day3.csv", header=None, usecols=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
bin = ""
data_counts = data.apply(pd.Series.value_counts)

data_max = data_counts.idxmax()
bin_max =data_max.array
res_max = int("".join(str(x) for x in bin_max), 2)

data_min = data_counts.idxmin()
bin_min =data_min.array
res_min = int("".join(str(x) for x in bin_min), 2)

print(res_max, res_min, res_max*res_min)
