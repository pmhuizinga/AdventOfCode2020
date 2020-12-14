"""
Advent of code
--- Day 3: Toboggan Trajectory ---
With the toboggan login problems resolved, you set off toward the airport. While travel by toboggan might be easy, it's certainly not safe: there's very minimal steering and the area is covered in trees. You'll need to see which angles will take you near the fewest trees.

Due to the local geology, trees in this area only grow on exact integer coordinates in a grid. You make a map (your puzzle input) of the open squares (.) and trees (#) you can see. For example:

..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#
These aren't the only trees, though; due to something you read about once involving arboreal genetics and biome stability, the same pattern repeats to the right many times:

..##.........##.........##.........##.........##.........##.......  --->
#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..
.#....#..#..#....#..#..#....#..#..#....#..#..#....#..#..#....#..#.
..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#
.#...##..#..#...##..#..#...##..#..#...##..#..#...##..#..#...##..#.
..#.##.......#.##.......#.##.......#.##.......#.##.......#.##.....  --->
.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#
.#........#.#........#.#........#.#........#.#........#.#........#
#.##...#...#.##...#...#.##...#...#.##...#...#.##...#...#.##...#...
#...##....##...##....##...##....##...##....##...##....##...##....#
.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#  --->
You start on the open square (.) in the top-left corner and need to reach the bottom (below the bottom-most row on your map).

The toboggan can only follow a few specific slopes (you opted for a cheaper model that prefers rational numbers); start by counting all the trees you would encounter for the slope right 3, down 1:

From your starting position at the top-left, check the position that is right 3 and down 1. Then, check the position that is right 3 and down 1 from there, and so on until you go past the bottom of the map.

The locations you'd check in the above example are marked here with O where there was an open square and X where there was a tree:

..##.........##.........##.........##.........##.........##.......  --->
#..O#...#..#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..
.#....X..#..#....#..#..#....#..#..#....#..#..#....#..#..#....#..#.
..#.#...#O#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#
.#...##..#..X...##..#..#...##..#..#...##..#..#...##..#..#...##..#.
..#.##.......#.X#.......#.##.......#.##.......#.##.......#.##.....  --->
.#.#.#....#.#.#.#.O..#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#
.#........#.#........X.#........#.#........#.#........#.#........#
#.##...#...#.##...#...#.X#...#...#.##...#...#.##...#...#.##...#...
#...##....##...##....##...#X....##...##....##...##....##...##....#
.#..#...#.#.#..#...#.#.#..#...X.#.#..#...#.#.#..#...#.#.#..#...#.#  --->
In this example, traversing the map using this slope would cause you to encounter 7 trees.

Starting at the top-left corner of your map and following a slope of right 3 and down 1, how many trees would you encounter?

Your puzzle answer was 274.

The first half of this puzzle is complete! It provides one gold star: *

--- Part Two ---
Time to check the rest of the slopes - you need to minimize the probability of a sudden arboreal stop, after all.

Determine the number of trees you would encounter if, for each of the following slopes, you start at the top-left corner and traverse the map all the way to the bottom:

Right 1, down 1.
Right 3, down 1. (This is the slope you already checked.)
Right 5, down 1.
Right 7, down 1.
Right 1, down 2.
In the above example, these slopes would find 2, 7, 3, 4, and 2 tree(s) respectively; multiplied together, these produce the answer 336.

What do you get if you multiply together the number of trees encountered on each of the listed slopes?
"""
import numpy as np
import math

slopes_test = [[1, 3], [3, 1]]
slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]

# read
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
        # print('shape: {}, col {}, rownr {}, val {}'.format(d.shape, col_pos, row_pos, val))
        row_pos = row_pos + down
        col_pos = col_pos + right

    print('result of right {}, down {} is {}'.format(right, down, val))
    return val

x = ([calc_trees(x[0], x[1]) for x in slopes])
y = 1
for result in x:
    y = result * y
print('total is {}'.format(y))