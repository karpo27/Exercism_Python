def classify(number):

    aliquot_sum = 0
    counter = 1
    if number > 0:
        while counter < number:
            if number % counter == 0:
                aliquot_sum = aliquot_sum + counter

            counter += 1
    else:
        raise ValueError("Classification is only possible for positive integers.")

    if aliquot_sum == number:
        return "perfect"
    elif aliquot_sum > number:
        return "abundant"
    else:
        return "deficient"
        
