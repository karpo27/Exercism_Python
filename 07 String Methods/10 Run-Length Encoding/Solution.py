def decode(string):
    if not string:
        return string

    decoded = []
    counter = ""
    for i in range(len(string)):
        if string[i].isdigit():
            counter += string[i]
        else:
            if not counter:
                decoded.append(string[i])
            else:
                decoded.append(int(counter) * string[i])
            counter = ""

    return "".join(decoded)


def encode(string):
    if not string:
        return string

    encoded = []
    counter = 0
    for i in range(len(string)):
        if i == 0:
            counter += 1
        elif string[i] == string[i - 1]:
            counter += 1
            if i == len(string) - 1:
                encoded.append(str(counter) + string[i - 1])
        else:
            if counter == 1:
                encoded.append(string[i - 1])
            else:
                encoded.append(str(counter) + string[i - 1])
            counter = 1
            if i == len(string) - 1:
                encoded.append(string[i])

    return "".join(encoded)
