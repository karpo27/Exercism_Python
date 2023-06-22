def value(colors):
    resistor_code = {
        "black": 0,
        "brown": 1,
        "red": 2,
        "orange": 3,
        "yellow": 4,
        "green": 5,
        "blue": 6,
        "violet": 7,
        "grey": 8,
        "white": 9
    }

    number = ""
    for i in colors:
        if i in resistor_code:
            if len(number) < 2:
                number = number + str(resistor_code[i])

    return int(number)
