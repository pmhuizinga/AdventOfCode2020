def prep_data(filepath):

    with open(filepath, 'r') as f:
        data = f.read()

    data2 = [[y.replace('bags', '').replace('bag', '').replace('no other', '0 no other').replace('.', '').strip() for y in
              x.split('contain')] for x in
             data.split('\n')]

    # make list of list of all source bags and all the bags it contains
    new_list = []
    for rule in data2:
        tmp_list = [rule[0]]
        content = rule[1].split(',')
        f = []
        for item in content:
            d = item.split()
            string = ''
            g = []
            for e in d:
                if e.isdigit():
                    g.append(int(e))
                else:
                    string = string + ' ' + e
            g.append(string.strip())
            f.append(g)
        tmp_list.append(f)
        new_list.append(tmp_list)

    # convert to a 1 on 1 relation including the number of bags
    list2 = []
    for x in new_list:
        for y in x[1]:
            l = [x[0], y[1], y[0]]
            list2.append(l)

    return list2

# recursive function for looping through the list
# counts every unique relation
def day7a(list, target_item_to_find, list_of_knowns=None, counter=0):

    if list_of_knowns is None:
        list_of_knowns = []
    for idx, combination in enumerate(list):
        if combination[1] == target_item_to_find:
            if len(set(list_of_knowns).intersection({combination[0]})) == 0:
                counter += 1
                list_of_knowns.append(combination[0])
                counter = day7a(list, combination[0], list_of_knowns, counter)

    return counter

a = r'data/aoc7.txt'
result = day7a(prep_data(a), 'shiny gold')
print('result of day 7a is: {}'.format(result))

"""
part 2
"""

testlist = [['shiny gold white', 'dark red', 2],
            ['dark red', 'dark orange', 2],
            ['dark orange', 'dark yellow', 2],
            ['dark yellow', 'dark green', 2],
            ['dark green', 'dark blue', 2],
            ['dark blue', 'dark violet', 2],
            ['dark violet', 'no other', 0]]

def day7b():

    return 4

