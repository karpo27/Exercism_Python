def saddle_points(matrix):
    if not matrix:
        return matrix

    test_list = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if j + 1 == len(matrix[i]):
                test_list.append(j + 1)

    if len(set(test_list)) != 1:
        raise ValueError("irregular matrix")

    n_rows = 0
    for y in range(len(matrix)):
        n_rows += 1

    new_list = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            c = 0
            for k in range(len(matrix[i])):
                if matrix[i][j] >= matrix[i][k]:
                    c += 1

            if c == len(matrix[i]):
                d = 0
                for x in range(len(matrix)):
                    for z in range(len(matrix[x])):
                        if j == z and matrix[i][j] <= matrix[x][z]:
                            d += 1
                            if d == n_rows:
                                new_list.append({"row": i + 1, "column": j + 1})

    return new_list
