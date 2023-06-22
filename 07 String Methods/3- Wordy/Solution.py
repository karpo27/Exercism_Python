def answer(question):

    if question == "What is?":
        raise ValueError("syntax error")

    question = ((question.removesuffix('?')).removeprefix('What is ')).split(' ')

    for i in question:
        if i == 'by':
            question.remove('by')

    number = 0
    for i in range(len(question)):
        if question[i].isdigit() == True:
            number += 1
        else:
            if question[i][0] == "-":
                number += 1

    if number == 0:
        raise ValueError("unknown operation")
    
    specials = ['plus', 'minus', 'multiplied', 'divided']
    for i in question:
        if i.isdigit() == False and i not in specials and i[0] != '-':
            raise ValueError("unknown operation")

    number = 0
    operations = 0
    for i in range(len(question)):
        if 0 <= number - operations <= 1:
            if question[i].isdigit() == True:
                number += 1
            else:
                if question[i][0] == "-":
                    number += 1
                else:
                    operations += 1
        else:
            raise ValueError("syntax error")

    if number != operations + 1:
        raise ValueError("syntax error")

    n = int(question[0])
    for i in range(len(question)):
        if question[i].isdigit() == False:
            if question[i] == 'plus':
                n = n + int(question[i + 1])
            elif question[i] == 'minus':
                n = n - int(question[i + 1])
            elif question[i] == 'multiplied':
                n = n * int(question[i + 1])
            elif question[i] == 'divided':
                n = n / int(question[i + 1])

    return n
