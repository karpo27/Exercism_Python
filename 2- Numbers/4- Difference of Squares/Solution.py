def square_of_sum(number):
    counter = 0
    sum = 0
    while counter <= number:
        sum = counter + sum
        counter = counter + 1

    return sum ** 2

def sum_of_squares(number):
    counter = 0
    sum = 0
    while counter <= number:
        sum = counter ** 2 + sum
        counter = counter + 1

    return sum

def difference_of_squares(number):
    return square_of_sum(number) - sum_of_squares(number)
