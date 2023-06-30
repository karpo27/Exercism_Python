def sum_of_multiples(limit, multiples):
    new_list = []
    for i in multiples:
        for j in range(1, limit):
            if i != 0 and j != 1 and j % i == 0:
                new_list.append(j)
            elif i == j:
                new_list.append(j)

    return sum(set(new_list))
    
