def steps(number):
    if number > 0 and isinstance(number, int):
        contador = 0
        while number > 1:
            if number % 2 == 0:
                number = number / 2
                contador = contador + 1

            elif number % 2 != 0:
                number = (number * 3) + 1
                contador = contador + 1

            elif number == 1:
                break

        return contador
    else:
        raise ValueError("Only positive integers are allowed")
