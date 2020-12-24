def prep_data(filepath):
    with open(filepath, 'r') as f:
        data = f.read()

    data2 = [[y for y in x.split(' ')] for x in data.split('\n')]

    for x in data2:
        x[1] = int(x[1])

    return data2


def day8a(data):
    lst = []
    i = 0
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

result = day8a(prep_data(r'data/aoc8.txt'))
print('result of day 8a is: {}'.format(result))
