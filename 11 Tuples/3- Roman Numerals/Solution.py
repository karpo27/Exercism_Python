def roman(number):
    code = {
        '1': ['I', 'X', 'C', 'M'],
        '4': ['IV', 'XL', 'CD'],
        '5': ['V', 'L', 'D'],
        '9': ['IX', 'XC', 'CM']
    }

    str_number = str(number)
    roman = ""
    c = 0
    for i in reversed(range(len(str_number))):
        print(i)
        if str_number[i] in code:
            roman = code[str_number[i]][c] + roman
            c += 1
        elif 1 < int(str_number[i]) < 4:
            roman = int(str_number[i]) * code['1'][c] + roman
            c += 1
        elif 5 < int(str_number[i]) <= 8:
            roman = code['5'][c] + (int(str_number[i]) - 5) * code['1'][c] + roman
            c += 1
        else:
            c += 1

    return roman
