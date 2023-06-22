def transform(legacy_data):

    data = {}
    items_list = []
    for i in legacy_data.values():
        for j in i:
            items_list.append(j)

    items_list.sort()
    for k in items_list:
        for x, z in legacy_data.items():
            for n in z:
                if k == n:
                    data.update({k.lower(): x})

    return data
    
