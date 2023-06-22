def flatten(iterable):

    step_1 = str(iterable)
    none = step_1.count('None')
    sqr_bracket = step_1.count('[')
    step_2 = step_1.replace('[', '', sqr_bracket)
    step_3 = step_2.replace(']', '', sqr_bracket)
    step_4 = step_3.replace('None', '', none)
    iterable = step_4.split(', ')

    new_list = []
    for i in range(len(iterable)):
        if iterable[i] != '':
            new_list.append(int(iterable[i]))

    return new_list
