import random
import string

class Robot:
    def __init__(self):
        self.name = self.reset()

    def reset(self):
        random.seed()
        letters = random.sample(string.ascii_uppercase, k=2)
        digits = random.sample(string.digits, k=3)

        self.name = ''.join(letters) + ''.join(digits)
        return self.name
