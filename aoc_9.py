def prep_data(filepath):
    with open(filepath, 'r') as f:
        data = f.read()

    data = data.split()
    return data

d = prep_data(r'test/aoc9.txt')

def aoc9a(data, preamble=5):
    length = len(data)


