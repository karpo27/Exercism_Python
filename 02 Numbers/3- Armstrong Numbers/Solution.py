def is_armstrong_number(number):
  
    digit = len(str(number))
    str_numb = str(number)
    counter = 1
    a = 0

    while counter <= digit:
        a = (int(str_numb[counter - 1])) ** digit + a
        counter = counter + 1

    if a == number:
        return True
    else:
        return False
