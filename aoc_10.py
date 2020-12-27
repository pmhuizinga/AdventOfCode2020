def prep_data(filepath):
    with open(filepath, 'r') as f:
        data = f.read()

    data = data.split()
    data = [int(x) for x in data]

    return data

d = prep_data(r'data/aoc10.txt')

def day10a(data):

    data.append(0)
    data.append(max(data) + 3)
    data.sort()
    data = list(set(data))

    j1 = 0
    j3 = 0

    for i in range(1, len(data)):

        diff = data[i] - data[i - 1]

        if diff == 1:
            j1 += 1
        elif diff == 3:
            j3 += 1

    return j1 * j3

day10a(d)
