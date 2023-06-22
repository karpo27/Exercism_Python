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
        tolerances = {
            "grey": 0.05,
            "violet": 0.1,
            "blue": 0.25,
            "green": 0.5,
            "brown": 1,
            "red": 2,
            "gold": 5,
            "silver": 10,
        }
        if len(colors) == 1:
            return f'0 ohms'

        comparator = len(colors) - 2
        number, unit, tolerance = "", "", ""
        for i in range(len(colors)):
            if i < comparator:
                number += str(resistor_code[colors[i]])
            elif i == comparator:
                number = int(number) * 10 ** resistor_code[colors[i]]
            else:
                tolerance += str(tolerances[colors[i]])

        if 1000 <= number < 10 ** 6:
            number /= 1000
            unit = "kilo"
        elif number > 10 ** 6:
            number /= (10 ** 6)
            unit = "mega"

        if number - int(number) == 0.0:
            number = int(number)

        return f'{number} {unit}ohms ±{tolerance}%'
