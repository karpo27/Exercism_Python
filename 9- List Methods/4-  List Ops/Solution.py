from functools import reduce

def append(list1, list2):
    for i in list2:
        list1.append(i)

    return list1

def concat(lists):

    step_1 = str(lists)
    sqr_bracket = step_1.count('[')
    step_2 = step_1.replace('[', '', sqr_bracket)
    step_3 = step_2.replace(']', '', sqr_bracket)
    lists = step_3.split(', ')

    new_list = []
    for i in range(len(lists)):
        if lists[i] != '':
            new_list.append(int(lists[i]))

    return new_list

def filter(function, list):
    new_list = []
    for i in list:
        if function(i) == True:
            new_list.append(i)

    return new_list

def length(list):
    return len(list)

def map(function, list):
    new_list = []
    for i in list:
        new_list.append(function(i))
        
    return new_list

def foldl(function, list, initial):
    if len(list) == 0:
        return initial

    result = reduce(function, list)

    return result + initial

def foldr(function, list, initial):
    if len(list) == 0:
        return initial

    result = reduce(function, list)

    return result + initial

def reverse(list):
    list.reverse()
    
    return list
    
