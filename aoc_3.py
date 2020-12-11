# -*- coding: utf-8 -*-
"""
Advent of code
day 3
"""
import numpy as np
import math

# vars
right = 3
down = 1

# read
aoc = r'aoc3.txt'
d = open(aoc, 'r')
data = d.readlines()

# data prep
# strip data and replace '.'  with 0 and '#' with 1
data = np.array([[b.replace('.', '0').replace('#', '1') for b in a.strip()] for a in data])

# the array needs to duplicated x times ('right' value times the number of rows)
nr_of_rows = len(data)
required_nr_of_columns = right * nr_of_rows
nr_of_duplications = math.ceil(required_nr_of_columns / data.shape[1])
d = data
for i in range(nr_of_duplications):
    d = np.concatenate([d, data], axis=1)

# loop through the array and sum all the ones
row_pos = 0
col_pos = 0
val = 0
for idx, row in enumerate(range(d.shape[0]-1)):
    col_pos = col_pos + right
    row_pos = row_pos + down
    val = val + int(d[row_pos][col_pos])
    print(row_pos, col_pos)

print(val)
