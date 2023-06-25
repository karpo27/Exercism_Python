class HighScores:
    def __init__(self, scores):
        self.scores = scores

    def latest(self):
        return self.scores[-1]

    def personal_best(self):
        return max(self.scores)

    def personal_top_three(self):
        top_three = self.scores.copy()
        top_three.sort(reverse=True)
        if len(top_three) >= 3:
            return top_three[:3]
        else:
            return top_three
            
