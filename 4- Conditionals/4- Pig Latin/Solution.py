def translate(text):
    text_1 = text.split()
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    specials = ['x', 'y', 'X', 'Y']
    cons = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'ñ', 'p', 'q', 'r', 's',
            't', 'v', 'w', 'z', 'B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M',
            'N', 'Ñ', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Z'
            ]
    
    counter_i = 0
    for i in text_1:
        counter_j = 0
        counter_m = 0
        counter_k = 0
        for j in vowels:
            if text_1[counter_i].startswith(vowels[counter_j]) == True:
                text_1[counter_i] = text_1[counter_i] + "ay"

            counter_j += 1

        for m in specials:
            if text_1[counter_i].startswith(specials[counter_m]) == True:
                if text_1[counter_i][1] in vowels:
                    text_1[counter_i] = text_1[counter_i].removeprefix(specials[counter_m]) + specials[counter_m] + "ay"
                else:
                    text_1[counter_i] = text_1[counter_i] + "ay"

            counter_m += 1

        for k in cons:
            if text_1[counter_i].startswith(cons[counter_k]) == True:
                if text_1[counter_i][1] == "q" and text_1[counter_i][2] == "u":
                    text_1[counter_i] = text_1[counter_i].removeprefix(cons[counter_k] + "qu") + cons[
                        counter_k] + "qu" + "ay"

                elif text_1[counter_i][1] in cons:
                    if text_1[counter_i][2] in cons:
                        if text_1[counter_i][2] != "y" or "Y":
                            temp = cons[counter_k] + text_1[counter_i][1] + text_1[counter_i][2]
                            text_1[counter_i] = text_1[counter_i].removeprefix(temp) + temp + "ay"

                        elif text_1[counter_i][2] == "y" or "Y":
                            temp = cons[counter_k] + text_1[counter_i][1]
                            text_1[counter_i] = text_1[counter_i].removeprefix(temp) + temp + "ay"

                    else:
                        temp = cons[counter_k] + text_1[counter_i][1]
                        text_1[counter_i] = text_1[counter_i].removeprefix(temp) + temp + "ay"

                elif text_1[counter_i].startswith("q") == True and text_1[counter_i][1] == "u":
                    text_1[counter_i] = text_1[counter_i].removeprefix("qu") + "qu" + "ay"

                else:
                    text_1[counter_i] = text_1[counter_i].removeprefix(cons[counter_k]) + cons[counter_k] + "ay"

            counter_k += 1

        counter_i += 1

    text_2 = " ".join(text_1)
    return text_2
