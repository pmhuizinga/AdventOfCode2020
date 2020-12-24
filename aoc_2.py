# -*- coding: utf-8 -*-
import numpy as np

# read
with open(r'data/aoc2.txt', 'r') as f:
    data = f.readlines()

data2 = np.array([ a.split(' ')[0].split('-') + a.split(' ')[1:] for a in data])

i = 0
for x in range(data2.shape[0]):
    if int(data2[x, 0]) <= data2[x, 3].count(data2[x, 2][0]) <= int(data2[x, 1]):
        i += 1

print(i)
