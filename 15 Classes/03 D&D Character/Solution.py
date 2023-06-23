import secrets
import math


def modifier(constitution):
    return math.floor((constitution - 10) / 2)


class Character:
    def __init__(self):
        dice = list(range(1, 7))
        stats = []
        for i in range(6):
            roll_dice = []
            for j in range(4):
                roll_dice.append(secrets.choice(dice))

            roll_dice.sort(reverse=True)
            stats.append(sum(roll_dice[:3]))

        self.strength, self.dexterity, self.constitution, self.intelligence, self.wisdom, self.charisma = stats
        self.hitpoints = 10 + modifier(self.constitution)

    def ability(self):
        return secrets.choice([self.strength, self.dexterity, self.constitution, self.intelligence, self.wisdom, self.charisma])
        
