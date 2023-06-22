def rows(letter):
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
               'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    step_2 = []
    for i in range(len(letters)):
        if letters[i] == letter:
            if i == 0:
                return [letters[i]]

            else:
                step_1 = letters[:i]
                temp = len(letters[:i + 1]) + len(letters[:i])
                center = letter + " " * (temp - 2) + letter

                c = 0
                d = 1
                for j in range(len(step_1)):
                    if j == 0:
                        step_2.append(" " * i + step_1[j] + " " * i)
                    else:
                        step_2.append(" " * (i - c) + step_1[j] + " " * d + step_1[j] + " " * (i - c))
                        d += 2
                    c += 1

                step_2.append(center)

    step_3 = step_2.copy()
    step_3.remove(center)
    step_3.reverse()
    result = step_2 + step_3

    return result
    
