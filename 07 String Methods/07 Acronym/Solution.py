def abbreviate(words):
    acronym = ""
    for i, char in enumerate(words):
        if char.isalpha():
            if i == 0:
                acronym += char
            elif not words[i - 1].isalpha() and words[i - 1] != "'":
               acronym += char.upper()

    return acronym
  
