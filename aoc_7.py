"""
--- Day 7: Handy Haversacks ---
You land at the regional airport in time for your next flight. In fact, it looks like you'll even have time to
grab some food: all flights are currently delayed due to issues in luggage processing.

Due to recent aviation regulations, many rules (your puzzle input) are being enforced about bags and their contents;
bags must be color-coded and must contain specific quantities of other color-coded bags. Apparently, nobody
responsible for these regulations considered how long they would take to enforce!

For example, consider the following rules:

light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.
These rules specify the required contents for 9 bag types. In this example, every faded blue bag is empty, every
vibrant plum bag contains 11 bags (5 faded blue and 6 dotted black), and so on.

You have a shiny gold bag. If you wanted to carry it in at least one other bag, how many different bag colors
would be valid for the outermost bag? (In other words: how many colors can, eventually, contain at least one
shiny gold bag?)

In the above rules, the following options would be available to you:

A bright white bag, which can hold your shiny gold bag directly.
A muted yellow bag, which can hold your shiny gold bag directly, plus some other bags.
A dark orange bag, which can hold bright white and muted yellow bags, either of which could then hold your shiny
gold bag.
A light red bag, which can hold bright white and muted yellow bags, either of which could then hold your
shiny gold bag. So, in this example, the number of bag colors that can eventually contain at least one shiny
gold bag is 4.

How many bag colors can eventually contain at least one shiny gold bag? (The list of rules is quite long;
make sure you get all of it.)
"""

# plan
# split records in source bag, target bag(s)
# the number of bags is not relevant
# create matrix

import numpy as np
import pandas as pd

# read
with open(r'data/aoc7_test.txt', 'r') as f:
    data = f.read()

data2 = [[y.replace('bags', '').replace('bag', '').replace('no other', '0 no other').replace('.', '').strip() for y in x.split('contain')] for x in
         data.split('\n')]

# make new list
new_list = []
for rule in data2:
    tmp_list = [rule[0]]
    content = rule[1].split(',')
    f = []
    for item in content:
        d = item.split()
        string = ''
        g = []
        for e in d:
            if e.isdigit():
                g.append(int(e))
            else:
                string = string + ' ' + e
        g.append(string.strip())
        f.append(g)
    tmp_list.append(f)
    new_list.append(tmp_list)


# # get all options
# options = []
# for x in new_list:
#     options.append(x[0])
#     for y in x[1]:
#         options.append(y[1])
#
# options = list(set(options))
# options.sort()
# nr_of_options = len(options)
#
# # make array
# array = np.zeros((nr_of_options, nr_of_options))
# # make dataframe
# df = pd.DataFrame(array, columns=options)
# df['index'] = options
# df.set_index(['index'], inplace=True)

# fill dataframe
list2 = []
for x in new_list:
    for y in x[1]:
        l = [x[0], y[1], y[0]]
        list2.append(l)

def recursive_shizzle(list, target_item_to_find, counter=0):
    print('-' * 60)
    print('target {}, çounter {}'.format(target_item_to_find, counter))
    for combination in list:
        # print(combination)
        if combination[1] == target_item_to_find:
            counter = recursive_shizzle(list, combination[0], counter + 1)
            print('combination[0] {}'.format(combination[0]))

    return counter

# testlist = [['a', 'b'],['c', 'a'], ['d', 'b'],['z', 'c']]
result = recursive_shizzle(list2, 'shiny gold')
result