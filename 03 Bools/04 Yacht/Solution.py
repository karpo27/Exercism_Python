YACHT = "YACHT"
ONES = "ONES"
TWOS = "TWOS"
THREES = "THREES"
FOURS = "FOURS"
FIVES = "FIVES"
SIXES = "SIXES"
FULL_HOUSE = "FULL_HOUSE"
FOUR_OF_A_KIND = "FOUR_OF_A_KIND"
LITTLE_STRAIGHT = "LITTLE_STRAIGHT"
BIG_STRAIGHT = "BIG_STRAIGHT"
CHOICE = "CHOICE"

def score(dice, category):
    if category == "ONES":
        qty_num_one = dice.count(1)
        if qty_num_one != 0:
            return qty_num_one * 1
        else:
            return 0

    elif category == "TWOS":
        qty_num_two = dice.count(2)
        if qty_num_two != 0:
            return qty_num_two * 2
        else:
            return 0

    elif category == "THREES":
        qty_num_three = dice.count(3)
        if qty_num_three != 0:
            return qty_num_three * 3
        else:
            return 0

    elif category == "FOURS":
        qty_num_four = dice.count(4)
        if qty_num_four != 0:
            return qty_num_four * 4
        else:
            return 0

    elif category == "FIVES":
        qty_num_five = dice.count(5)
        if qty_num_five != 0:
            return qty_num_five * 5
        else:
            return 0

    elif category == SIXES:
        qty_num_six = dice.count(6)
        if qty_num_six != 0:
            return qty_num_six * 6
        else:
            return 0

    elif category == "FULL_HOUSE":
        for i in dice:
            qty_num = dice.count(i)
            if qty_num == 3:
                dice_r = dice
                dice_r.remove(i)
                dice_r.remove(i)
                dice_r.remove(i)
                for j in dice_r:
                    qty_num_r = dice_r.count(j)
                    if qty_num_r == 2:
                        return qty_num * i + qty_num_r * j            
        else:
            return 0

    elif category == "FOUR_OF_A_KIND":
        for i in dice:
            qty_num = dice.count(i)
            if qty_num == 4 or qty_num == 5:
                return 4 * i
            else:
                return 0

    elif category == "LITTLE_STRAIGHT":
        if sorted(dice) == [1, 2, 3, 4, 5]:
            return 30
        else:
            return 0

    elif category == "BIG_STRAIGHT":
        if sorted(dice) == [2, 3, 4, 5, 6]:
            return 30
        else:
            return 0

    elif category == "CHOICE":
        return sum(dice)

    elif category == "YACHT":
        for i in dice:
            qty_num = dice.count(i)
            if qty_num == 5:
                return 50
            else:
                return 0
 
