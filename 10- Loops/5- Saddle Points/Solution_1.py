 import numpy as np


def saddle_points(matrix):
    arr = np.array(matrix)
    if arr.shape[0] != arr.shape[1]:
        raise ValueError("irregular matrix")

    dict_rc = {}
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            c = 0
            for k in range(len(arr[i])):
                if arr[i][j] >= arr[i][k]:
                    c += 1

            if c == arr.shape[1]:
                for x in range(len(arr)):
                    for z in range(len(arr[x])):
                        if j == z and arr[i][j] <= arr[x][z]:
                            c += 1
                            if c == arr.shape[1] * 2:
                                dict_rc.update({(i + 1, j + 1): arr.shape[1]})

    return dict_rc
    
