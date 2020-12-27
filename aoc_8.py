def prep_data(filepath):
    with open(filepath, 'r') as f:
        data = f.read()

    data2 = [[y for y in x.split(' ')] for x in data.split('\n')]

    # make integer
    for x in data2:
        x[1] = int(x[1])

    return data2

d = prep_data(r'test/aoc8.txt')

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

def find_bad_statement(data, index):
    data_lenght = len(data)
    accumulator = 0
    counter = 0
    list = set()
    status = False

    while 0 <= counter < data_lenght:
        step = data[counter]
        action = step[0]
        value = step[1]

        if counter in list:
            # print('item already handled')
            status = False
            return status, counter, accumulator
        else:
            list.add(counter)

        if counter == index:
            if action == 'jmp':
                # print(f"changing jpm to nop at index {counter}")
                action = 'nop'
            elif action == 'nop':
                # print(f'changing nop to jmp at index {counter}')
                action = 'jmp'

        if action == 'jmp':
            counter += value
            continue
        elif action == 'nop':
            pass
        elif action == 'acc':
            accumulator += value

        counter += 1

    return True, counter, accumulator


def day8b(data):
    for i in range(len(data)):
        if data[0] != 'acc':
            result = find_bad_statement(data, i)
            if result[0]:
                print('the result is {}'.format(result[2]))
                break

    return result[2]

d = prep_data(r'data/aoc8.txt')

r = day8b(d)