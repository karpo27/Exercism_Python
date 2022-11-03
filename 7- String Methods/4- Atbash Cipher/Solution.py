def encode(plain_text):
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
               't', 'u', 'v', 'w', 'x', 'y', 'z']

    cipher = letters.copy()
    cipher.sort(reverse=True)
    plain_text = plain_text.lower()

    new_text = ""
    for i in range(len(plain_text)):
        if plain_text[i].isdigit() == True:
            new_text = new_text + plain_text[i]
        for j in range(len(letters)):
            if plain_text[i] == letters[j]:
                new_text = new_text + cipher[j]

    text_list = list(new_text)
    last_list = []
    for i in range(len(text_list)):
        if i % 5 == 0 and i != 0:
            last_list.append(' ')
            last_list.append(text_list[i])
        else:
            last_list.append(text_list[i])

    return "".join(last_list)

def decode(ciphered_text):
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
               't', 'u', 'v', 'w', 'x', 'y', 'z']

    cipher = letters.copy()
    cipher.sort(reverse=True)

    new_text = ""
    for i in range(len(ciphered_text)):
        if ciphered_text[i].isdigit() == True:
            new_text = new_text + ciphered_text[i]
        for j in range(len(cipher)):
            if ciphered_text[i] == cipher[j]:
                new_text = new_text + letters[j]

    return new_text
  
