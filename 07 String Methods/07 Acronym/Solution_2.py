def abbreviate(words):
    acronym = []
    previous_char = ''

    for char in words:
        if char.isalpha() and (not previous_char.isalpha() and previous_char != "'"):
            acronym.append(char.upper())

        previous_char = char

    return ''.join(acronym)
