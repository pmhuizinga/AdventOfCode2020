def prep_data(filepath):
    with open(filepath, 'r') as f:
        data = f.read()

    data = data.split()
    data = [int(x) for x in data]
    data.append(0)
    data.append(max(data) + 3)
    data.sort()
    data = list(set(data))

    return data


d = prep_data(r'test/aoc10.txt')


def day10a(data):
    j1 = 0
    j3 = 0

    for i in range(1, len(data)):

        diff = data[i] - data[i - 1]

        if diff == 1:
            j1 += 1
        elif diff == 3:
            j3 += 1

    return j1 * j3


def day10b(data):
    forward = 4
    total = 1
    for i in range(0, len(data)):
        # check how many options there are
        # first look at the next 3 items
        data_to_check = set(data[i + 1: i + forward])
        # make set of possibilities
        options = set(range(data[i]+1, data[i]+forward, 1))
        # count match
        count = len(data_to_check.intersection(options))
        print('value: {}, data_to_check {}, options {}, overlap {}'.format(data[i], data_to_check, options, count))
        if count > 1:
            total += count

    return total

print(day10a(d))
print(day10b(d))
