def prep_data(filepath):
    with open(filepath, 'r') as f:
        data = f.read()

    data = data.split()
    data = [int(x) for x in data]

    return data

d = prep_data(r'test/aoc9.txt')

def find_values(data, summed_value):
    for x in data:
        if summed_value - x in data:
            return True

    return False


def day9a(data, preamble=25):
    length = len(data)

    for i in range(preamble, length):

        inputlist = data[i - preamble:i]
        if find_values(inputlist, data[i]) == False:
            return data[i]


def day9b(data, preamble=25):

    invalid_number = day9a(d, preamble)

    # 1 find position in list
    position_of_invalid_number = ([i for i, x in enumerate(data) if x == invalid_number])[0]

    for i in range(0, position_of_invalid_number):
        for j in range(i + 1, position_of_invalid_number):
            if sum(data[i:j]) == invalid_number:
                return min(data[i:j]) + max(data[i:j])
                break


print(day9a(d, preamble=5))
print(day9b(d, preamble=5))
