# -*- coding: utf-8 -*-

# read
with open(r'data/aoc1.txt', 'r') as f:
    data = f.read().split()

data = set(data)

# prepare
data = [int(x) for x in data]

# code
for x in data:
    if 2020 - x in data:
        y = 2020 - x
        print('numbers {} and {} add up to 2020, cumulative is {}'.format(x, y, (x*y)))
        
for x in data:
    for y in data:
        if 2020 - x - y in data:
            z = 2020 - x - y
            print('numbers {}, {} and {} add up to 2020, cumulative is {}'.format(x, y, z, (x*y*z)))
            

            



        
