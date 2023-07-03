def cipher_text(plain_text):
    new_text = [char.lower() for char in plain_text if char.isalnum()]
    new_text = "".join(new_text)

    if len(new_text) <= 1:
        return new_text

    c, r = 1, 1
    while not c * r >= len(new_text):
        if c <= r:
            c += 1
        elif c - r >= 1:
            r += 1

    new_text += " " * (r * c - len(new_text))

    encoded = " ".join([new_text[i::c] for i in range(c)])

    return encoded
  
