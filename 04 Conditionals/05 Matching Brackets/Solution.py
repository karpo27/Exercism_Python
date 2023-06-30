def is_paired(input_string):
    pairs = {"{": "}", "(": ")", "[": "]"}
    brackets = []
    for char in input_string:
        if char in ("[", "{", "("):
            brackets.append(char)
        elif char in ("]", "}", ")"):
            try:
                open_br = brackets.pop()
            except:
                return False
            if not char == pairs[open_br]:
                return False
    return not brackets 
