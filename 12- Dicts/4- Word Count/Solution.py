def count_words(sentence):
    step_1 = sentence.lower()
    step_2 = ""
    for i in range(len(step_1)):
        if i != 0 and i != len(step_1) - 1 and step_1[i] == "'" and step_1[i - 1].isalpha() and step_1[i + 1].isalpha():
            step_2 += step_1[i]
        elif step_1[i].isalpha() or step_1[i].isdigit():
            step_2 += step_1[i]
        else:
            step_2 += " "

    sent_list = step_2.split()
    sent_dict = {}
    for i in range(len(sent_list)):
        if sent_list[i] not in sent_dict.keys():
            sent_dict.update({sent_list[i]: sent_list.count(sent_list[i])})

    return sent_dict
    
