def prep_data(filepath):
    with open(filepath, 'r') as f:
        data = f.read()

    data = data.split()
    data = [int(x) for x in data]

    return data


d = prep_data(r'data/aoc9.txt')


def find_values(data, summed_value):
    for x in data:
        if summed_value - x in data:
            # y = summed_value - x
            return True

    return False


def day9a(data, preamble=25):
    length = len(data)

    for i in range(preamble, length):

        inputlist = data[i - preamble:i]
        if find_values(inputlist, data[i]) == False:
            return data[i]


print(day9a(d))

def day9b(data):
    invalid_number = day9a(d)
    # 69316178
    # 1 find position in list
    position_of_invalid_number = ([i for i, x in enumerate(data) if x == invalid_number])[0]
    # print(position_of_invalid_number)

    for i in range(0, position_of_invalid_number):
        for j in range(i + 1, position_of_invalid_number):
            if sum(data[i:j]) == invalid_number:
                # print(data[i:j])
                return min(data[i:j]) + max(data[i:j])
                break

print(day9b(d))
