# read
with open(r'data/aoc5.txt', 'r') as f:
    data = f.read()

data = data.split('\n')

# list of all seat id's (row * 8 + seat number)
list_seat_id = []
# array of row, seat combinations
seat_list = []


def calc_pos(x, y, char):
    z = (y - x) / 2
    if char == 'F' or char == 'L':
        y = y - z
    else:
        x = x + z

    return x, y


# for each boarding pass code
for boardingpass in data:
    x = 0
    y = 128
    a = 0
    b = 8
    # for each character in x
    for char in boardingpass:
        # if character is not equal to L or R
        if char != 'L' and char != 'R':
            x, y = calc_pos(x, y, char)
        else:
            a, b = calc_pos(a, b, char)

    seat_id = int(x * 8 + a)
    list_seat_id.append(seat_id)
    seat_list.append([x, a])
    print('boardingpass {} has row {} and seat {} and seat id {}'.format(boardingpass, int(x), int(a), int(seat_id)))

print('the highest seat id is {}'.format(max(list_seat_id)))

# get unique rows
rows = set([x[0] for x in seat_list])
# create dictionary
D = {}
# populate dictionary with keys
[D.update({int(x): []}) for x in rows]
# populate dictionary with values
[D[x[0]].append(int(x[1])) for x in seat_list]

for x in rows:
    if min(rows) < x < max(rows):
        # find row
        if len(D[x - 1]) > len(D[x]) < len(D[x + 1]):
            # find seat
            seats = [0, 1, 2, 3, 4, 5, 6, 7]
            missing = list(set(seats) - set(D[x]))[0]
            seat_id = x * 8 + missing
            print('row is {}'.format(x))
            print('seat is {}'.format(missing))
            print('seat id is {}'.format(seat_id))
