def cipher_text(plain_text):
    new_text = []
    for char in plain_text:
        if char.isalnum():
            new_text.append(char.lower())

    new_text = "".join(new_text)
    if not new_text or len(new_text) == 1:
        return new_text

    c, r = 1, 1
    while not c * r >= len(new_text):
        if c <= r:
            c += 1
        elif c - r >= 1:
            r += 1

    while len(new_text) < r * c:
        new_text += " "

    encoded = ""
    for i in range(c):
        for j in range(0, len(new_text), c):
            if j + c >= len(new_text) and not i == c - 1:
                encoded += new_text[i + j] + " "
            else:
                encoded += new_text[i + j]

    return encoded
  
