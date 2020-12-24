# read
def prep_data(filepath):

    with open(filepath, 'r') as f:
        data = f.read()

    data2 = data.split('\n')
    # append emtpy item for use in loop
    data2.append('')

    # make list, split by blank records
    d = []
    e = []
    y = ''
    z = []
    for x in data2:
        if x == '':
            d.append(y)
            e.append(z)
            y = ''
            z = []
        else:
            y = str(x) + str(y)
            z.append(str(x))

    return d, e

def day6a(data):

    total = sum([len(set(x)) for x in data[0]])

    return total

result = day6a(prep_data(r'data/aoc6.txt'))

print('result of day 6a is {}'.format(result))

"""
part 2
"""

def day6b(data):
    counter = 0
    for x in data[1]:
        z = set(x[0])
        for y in range(len(x)):
            z = set(x[y]).intersection(z)
        counter += len(z)

    return counter

result = day6b(prep_data(r'data/aoc6.txt'))
print('result of day 6b is {}'.format(result))

