def is_valid(isbn):

    list_isbn = list(isbn)

    for i in list_isbn:
        if i == "-":
            list_isbn.remove("-")

    if "X" in list_isbn:
        list_isbn.remove("X")
        list_isbn.append("10")

    if len(list_isbn) != 10:
        return False

    for i in list_isbn:
        if i.isdigit() != True:
            return False

    c = 0
    for i, j in zip(list_isbn, reversed(range(11))):
        c = c + int(i) * j

    if c % 11 == 0:
        return True
    else:
        return False
