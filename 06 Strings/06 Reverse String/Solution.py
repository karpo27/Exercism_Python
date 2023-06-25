def reverse(text):
    reversed_text = ""
    for i in reversed(range(len(text))):
        reversed_text += text[i]

    return reversed_text
