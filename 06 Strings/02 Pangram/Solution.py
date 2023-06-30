def is_pangram(sentence):
    lower_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                     't', 'u', 'v', 'w', 'x', 'y', 'z'
                     ]
    upper_letters = ((','.join(lower_letters)).upper()).split(',')

    for i in upper_letters:
        lower_letters.append(i)

    letters = lower_letters

    z = 0
    for j in letters:
        if j in sentence:
            if j in lower_letters and j.upper() not in sentence:
                z += 1
            elif j in upper_letters and j.lower() not in sentence:
                z +=1
            else:
                pass

    if sentence != '' and z >= len(letters) / 2:
        return True
    else:
        return False
