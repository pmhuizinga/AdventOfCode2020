# plan
# - split records in source bag, target bag(s)
# - the number of bags is not relevant

# read
with open(r'data/aoc7_test.txt', 'r') as f:
    data = f.read()

data2 = data.split('\n')
data2 = [x.split('contain') for x in data2]
data2 = [[y.replace('bags', 'bag').replace('.', '').strip() for y in x] for x in data2]

data2