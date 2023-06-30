def get_list_of_wagons(*args):
    return list(args)

def fix_list_of_wagons(each_wagons_id, missing_wagons):
    a, b, c, *rest = each_wagons_id
    result = [c]
    result.extend(missing_wagons + rest + [a, b])
    
    return result

def add_missing_stops(*args, **kwargs):
    result_dict = {}
    for i in range(len(args)):
        if i == 0:
            for j, k in args[i].items():
                result_dict[j] = k

    new_list = []
    for i in kwargs.values():
        new_list.append(i)

    result_dict['stops'] = new_list

    return result_dict
    
        
def extend_route_information(route, more_route_information):
    return {**route, **more_route_information}

def fix_wagon_depot(wagons_rows):
    list_1 = []
    list_2 = []
    list_3 = []
    for i in range(len(wagons_rows)):
        for j in range(len(wagons_rows[i])):
            if j == 0:
                list_1.append(wagons_rows[i][j])
            elif j == 1:
                list_2.append(wagons_rows[i][j])
            elif j == 2:
                list_3.append(wagons_rows[i][j])

    result = [list_1, list_2, list_3]

    return result
    
