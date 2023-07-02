class Allergies:
    def __init__(self, score):
        self.score = score
        self.allergies_scores = {
            1: "eggs",
            2: "peanuts",
            4: "shellfish",
            8: "strawberries",
            16: "tomatoes",
            32: "chocolate",
            64: "pollen",
            128: "cats"
        }

    def allergic_to(self, item):
        return item in self.lst

    @property
    def lst(self):
        add_scores = 256
        while self.score > add_scores:
            self.allergies_scores[add_scores] = ""
            add_scores += add_scores

        allergies = []
        for score in reversed(self.allergies_scores.keys()):
            if score <= self.score:
                self.score -= score
                if self.allergies_scores[score] != "":
                    allergies.append(self.allergies_scores[score])

        return allergies
        
