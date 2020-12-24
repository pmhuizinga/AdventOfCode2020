# read
with open(r'data/aoc6.txt', 'r') as f:
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

total = sum([len(set(x)) for x in d])
print('the sum of counts is {}'.format(total))
print('-' * 30)

"""
part 2
"""

counter = 0
for x in e:
    z = set(x[0])
    for y in range(len(x)):
        z = set(x[y]).intersection(z)
    counter += len(z)

print('counter is {}'.format(counter))

