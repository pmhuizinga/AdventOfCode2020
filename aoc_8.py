def prep_data(filepath):
    with open(filepath, 'r') as f:
        data = f.read()

    data2 = [[y for y in x.split(' ')] for x in data.split('\n')]

    # make integer
    for x in data2:
        x[1] = int(x[1])

    return data2


def day8a(data, i=0, lst=[]):

    accumulator = 0
    while i not in lst:
        lst.append(i)
        next_step = data[i]
        if next_step[0] == 'nop':
            i += 1
        if next_step[0] == 'acc':
            i += 1
            accumulator += next_step[1]
        if next_step[0] == 'jmp':
            i += next_step[1]

    return accumulator


def test_loop(val, data, i, lst):
    # return True if result does not end in endless loop

    if val == 'nop':
        data[i][0] == 'jmp'
    if val == 'jmp':
        data[i][0] == 'nop'

    next_step = data[i]

    while i not in lst:
        lst.append(i)

        if next_step[0] == 'nop':
            i += 1
        if next_step[0] == 'acc':
            i += 1
        if next_step[0] == 'jmp':
            i += next_step[1]

        next_step = data[i]

    return

def day8b(data):
    lst = []
    i = 0
    accumulator = 0
    last_step = len(data) - 1
    while i < last_step:
        lst.append(i)
        next_step = data[i]
        if next_step[0] == 'acc':

            i += 1
            accumulator += next_step[1]

        if next_step[0] == 'nop':
            # check if the program finishes when changed to 'jmp'
            if test_loop('nop', data, i, lst) == True:
                i += next_step[1]
            else:
                i += 1

        if next_step[0] == 'jmp':

            if test_loop('jmp', data, i, lst) == True:
                i += 1
            else:
                i += next_step[1]

    return accumulator, lst


result = day8a(prep_data(r'data/aoc8.txt'))
print('result of day 8a is: {}'.format(result))

# result = day8b(prep_data(r'test/aoc8_test.txt'))
# print('result of day 8b is: {}. Last position is {}'.format(result[0], result[1][-2]))

data = prep_data(r'test/aoc8_test.txt')
