import numpy as np
import math

slopes_test = [[1, 3], [3, 1]]
slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]

# read
with open(r'data/aoc3.txt', 'r') as f:
    data = f.readlines()

# strip data and replace '.'  with 0 and '#' with 1
data = np.array([[b.replace('.', '0').replace('#', '1') for b in a.strip()] for a in data])

nr_of_rows, nr_of_columns = data.shape

def calc_trees(right, down):

    print('running procedure for right {} and down {}'.format(right, down))

    # caculate slope
    # if slope is 3 this means there are three times more columns required then rows
    slope = right/down
    print('slope is {}'.format(slope))

    required_nr_of_columns = nr_of_rows * slope
    nr_of_duplications = math.ceil(required_nr_of_columns / nr_of_columns)

    if nr_of_duplications > 1:
        print('required number of columns is {} so it needs to be duplicated {} times'.format(required_nr_of_columns,
                                                                                              nr_of_duplications))
        d = data
        for i in range(nr_of_duplications):
            d = np.concatenate([d, data], axis=1)

    print('the shape of data is {}'.format(d.shape))

    # loop through the array and sum all the ones
    col_pos = 0
    val = 0
    row_pos = 0
    while row_pos < nr_of_rows:

        if row_pos > nr_of_rows:
            row_pos = nr_of_rows

        val = val + int(d[row_pos][col_pos])
        row_pos = row_pos + down
        col_pos = col_pos + right

    print('result of right {}, down {} is {}'.format(right, down, val))
    return val

x = ([calc_trees(x[0], x[1]) for x in slopes])
y = 1
for result in x:
    y = result * y
print('total is {}'.format(y))