SUBLIST = 'SUBLIST'
SUPERLIST = 'SUPERLIST'
EQUAL = 'EQUAL'
UNEQUAL = 'UNEQUAL'

def sublist(list_one, list_two):
    if list_one == list_two:
        return EQUAL

    for n in range(len(list_two)):
        if list_one == list_two[n: n + len(list_one)]:
            return SUBLIST

    for n in range(len(list_one)):
        if list_two == list_one[n: n + len(list_two)]:
            return SUPERLIST
    return UNEQUAL
