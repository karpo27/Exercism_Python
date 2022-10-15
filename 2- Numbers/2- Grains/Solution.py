def square(number):
    
    if number == 1:       
        return number
        
    elif 2 <= number <= 64:
        return 2 * square(number - 1)
        
    else:
        raise ValueError("square must be between 1 and 64")

def total():

    lista = list(range(1, 65))
    total = sum(map(square, lista))
    return total
