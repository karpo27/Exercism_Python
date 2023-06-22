def is_isogram(string):
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                     't', 'u', 'v', 'w', 'x', 'y', 'z'
                     ]

    c = 0
    for j in range(len(letters)):
        if letters[j] in string and string.count(letters[j]) > 1:
            c += 1
        elif letters[j].upper() in string and string.count(letters[j].upper()) + string.count(letters[j]) > 1:
            c += 1

    if c == 0:
        return True
    else:
        return False
