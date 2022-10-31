def rotate(text, key):
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
               't', 'u', 'v', 'w', 'x', 'y', 'z']
    specials = ["'", " ", ".", "!", ",", "?"]

    new_text = ""
    for i in text:
        if i in specials or i.isdigit() == True:
            new_text = new_text + i
        for j in range(0, len(letters)):
            if i == letters[j] or i == letters[j].upper():
                if j + key >= 26:
                    new_text = new_text + letters[key - (len(letters) - j)]
                else:
                    new_text = new_text + letters[j + key]

    last_text = ""
    for i in range(0, len(text)):
        for j in range(0, len(new_text)):
            if i == j:
                if text[i].isupper() == True:
                    last_text = last_text + new_text[j].upper()
                else:
                    last_text = last_text + new_text[j]

    return last_text
