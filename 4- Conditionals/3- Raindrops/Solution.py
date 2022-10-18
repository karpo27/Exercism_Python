def convert(number):
    n_3 = number % 3
    n_5 = number % 5
    n_7 = number % 7
    list_1 = [n_3, n_5, n_7]
    list_2 = ["Pling", "Plang", "Plong"]
    result = ""
    counter = 0
    for i in list_1:
        if i == 0:
            result = result + list_2[counter]
        counter += 1

    if result != "":
        return result
    else:
        return str(number)
      
