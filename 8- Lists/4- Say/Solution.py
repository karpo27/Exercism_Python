def say(number):
    
    dictionary_1 = {
        "0": "zero",
        "1": "one",
        "2": "two",
        "3": "three",
        "4": "four",
        "5": "five",
        "6": "six",
        "7": "seven",
        "8": "eight",
        "9": "nine"
    }
    dictionary_2 = {
        "10": "ten",
        "11": "eleven",
        "12": "twelve",
        "13": "thirteen",
        "14": "fourteen",
        "15": "fifteen",
        "16": "sixteen",
        "17": "seventeen",
        "18": "eighteen",
        "19": "nineteen",
        "20": "twenty",
        "30": "thirty",
        "40": "forty",
        "50": "fifty",
        "60": "sixty",
        "70": "seventy",
        "80": "eighty",
        "90": "ninety"
    }
    
    str_number = str(number)
    if number < 0:
        raise ValueError("input out of range")
    elif number > 999999999999:
        raise ValueError("input out of range")
        
    step_1 = ""
    th = " thousand " + str_number[-3:]
    mi = " million " + str_number[-6:-3] + th
    bi = " billion " + str_number[-9:-6] + mi
    
    if 1 <= len(str_number) <= 3:
        step_1 = str_number
    elif 4 <= len(str_number) < 7:
        step_1 = str_number[-len(str_number):-3] + th
    elif 7 <= len(str_number) < 10:
        step_1 = str_number[-len(str_number):-6] + mi
    elif 10 <= len(str_number) < 13:
        step_1 = str_number[-len(str_number):-9] + bi
        
    step_1 = step_1.split()
    step_2 = []
    
    for z in range(len(step_1)):
        if step_1[z].isdigit() == True:
            if len(step_1[z]) == 3:
                if step_1[z][:2] == '00' and step_1[z][2] != '0':
                    step_2.append(step_1[z][2])
                elif step_1[z][0] == '0' and step_1[z][1] != '0':
                    step_2.append(step_1[z][1] + step_1[z][2])
                elif step_1[z][0] != '0' and step_1[z][1:] == '00':
                    step_2.append(step_1[z][0])
                    step_2.append('hundred')
                elif step_1[z][:2] != '00':
                    step_2.append(step_1[z][0])
                    step_2.append('hundred')
                    step_2.append(step_1[z][1] + step_1[z][2])
            else:
                step_2.append(step_1[z])
        else:
            if step_1[z] == 'million' and step_1[z-1] == '000':
                pass
            elif step_1[z] == 'thousand' and step_1[z-1] == '000':
                pass
            else:
                step_2.append(step_1[z])
                
    step_3 = []
    for k in range(len(step_2)):
        if step_2[k].isdigit() == True:
            if step_2[k] in dictionary_1:
                step_3.append(dictionary_1[step_2[k]])
            elif step_2[k] in dictionary_2:
                step_3.append(dictionary_2[step_2[k]])
            else:
                for i, j in dictionary_2.items():
                    if str(i)[0] == step_2[k][0]:
                        for x, y in dictionary_1.items():
                            if str(x)[0] == step_2[k][1]:
                                step_3.append(f'{j}-{y}')
        else:
            step_3.append(step_2[k])
            
    result = " ".join(step_3)
    return result
    
