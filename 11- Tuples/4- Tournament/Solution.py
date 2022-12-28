def tally(rows):
    stats = {}
    table = []   # 31
    new_list = []
    first_row = ["Team", "MP", "W", "D", "L", "P"]
    first_row[0] = first_row[0] + (31 - len(first_row[0])) * " "
    for i in range(len(rows)):
        temp_list = rows[i].split(";", 2)
        for j in range(len(temp_list)):
            if temp_list[j] not in stats.keys() and j != 2:
                if temp_list[2] == "win":
                    if j == 0:
                        stats.update({temp_list[j]: [1, 1, 0, 0, 3]})
                    elif j == 1:
                        stats.update({temp_list[j]: [1, 0, 0, 1, 0]})
                elif temp_list[2] == "loss":
                    if j == 0:
                        stats.update({temp_list[j]: [1, 0, 0, 1, 0]})
                    elif j == 1:
                        stats.update({temp_list[j]: [1, 1, 0, 0, 3]})
                elif temp_list[2] == "draw":
                    stats.update({temp_list[j]: [1, 0, 1, 0, 1]})
            elif temp_list[j] in stats.keys() and j != 2:
                for x, y in stats.items():
                    if x == temp_list[j]:
                        if temp_list[2] == "win":
                            if j == 0:
                                y[:] = [y[0] + 1, y[1] + 1, y[2] + 0, y[3] + 0, y[4] + 3]
                                stats.update({temp_list[j]: y})
                            elif j == 1:
                                y[:] = [y[0] + 1, y[1] + 0, y[2] + 0, y[3] + 1, y[4] + 0]
                                stats.update({temp_list[j]: y})
                        elif temp_list[2] == "loss":
                            if j == 0:
                                y[:] = [y[0] + 1, y[1] + 0, y[2] + 0, y[3] + 1, y[4] + 0]
                                stats.update({temp_list[j]: y})
                            elif j == 1:
                                y[:] = [y[0] + 1, y[1] + 1, y[2] + 0, y[3] + 0, y[4] + 3]
                                stats.update({temp_list[j]: y})
                        elif temp_list[2] == "draw":
                            y[:] = [y[0] + 1, y[1] + 0, y[2] + 1, y[3] + 0, y[4] + 1]
                            stats.update({temp_list[j]: y})

    for i, j in stats.items():
        temp = {i: j}
        temp["Points"] = j[4]
        temp["Name"] = i
        new_list.append(temp)

    def sort_points(x):
        return x["Points"]

    def sort_alpha(x):
        return x["Name"]

    new_list.sort(key=sort_alpha)
    new_list.sort(reverse=True, key=sort_points)


    print(new_list)

    for i in range(len(new_list)):
        new_list[i].pop("Points")
        new_list[i].pop("Name")

    print(new_list)
    board_1 = "{}" + "| {} " + "|  {} " + "|  {} " + "|  {} " + "|  {}"
    board_2 = "{}" + "|{} " + "|{} " + "|{} " + "|{} " + "|{}"
    table.append(board_1.format(*first_row))

    for i in range(len(new_list)):
        for j, k in new_list[i].items():
            temp = [
                    j + (31 - len(j)) * " ",
                    (3 - len(str(k[0]))) * " " + str(k[0]),
                    (3 - len(str(k[1]))) * " " + str(k[1]),
                    (3 - len(str(k[2]))) * " " + str(k[2]),
                    (3 - len(str(k[3]))) * " " + str(k[3]),
                    (3 - len(str(k[4]))) * " " + str(k[4])
                    ]
            table.append(board_2.format(*temp))

    return table
