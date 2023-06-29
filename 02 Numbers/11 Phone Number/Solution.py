class PhoneNumber:
    def __init__(self, number):
        cleaned = ""
        for char in number:
            if char.isdigit():
                cleaned += char
            elif char.isalpha():
                raise ValueError("letters not permitted")
            elif char not in ["-", ".", " ", "(", ")", "+"]:
                raise ValueError("punctuations not permitted")
            
        if len(cleaned) < 10:
            raise ValueError("must not be fewer than 10 digits")
        elif len(cleaned) == 11 and cleaned[0] != "1":
            raise ValueError("11 digits must start with 1")
        elif len(cleaned) > 11:
            raise ValueError("must not be greater than 11 digits")
        elif len(cleaned) == 11:
            cleaned = cleaned[1:]

        for i, char in enumerate(cleaned):
            if i == 0:
                if char == "0":
                    raise ValueError("area code cannot start with zero")
                elif char == "1":
                    raise ValueError("area code cannot start with one")
            elif i == 3:
                if char == "0":
                    raise ValueError("exchange code cannot start with zero")
                elif char == "1":
                    raise ValueError("exchange code cannot start with one")

        self.number = cleaned
        self.area_code = self.number[:3]

    def pretty(self):
        return f'({self.number[:3]})-{self.number[3:6]}-{self.number[6:]}'
        
