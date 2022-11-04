import itertools
from functools import reduce

def append(list1, list2):
    for i in list2:
        list1.append(i)

    return list1

def concat(lists):
    merged = list(itertools.chain(*lists))

    return merged

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
    
