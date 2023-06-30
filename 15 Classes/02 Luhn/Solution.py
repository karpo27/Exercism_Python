class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num

    def valid(self):
        new_num = ""
        for num in self.card_num:
            if num.isdigit():
                new_num += num
            elif num == " ":
                pass
            else:
                return False

        if len(new_num) == 1:
            return False
        
        if len(new_num) % 2 == 0:
            start = 0
        else:
            start = 1

        total_sum = 0
        counter = 0
        for i in range(len(new_num)):
            if (start + counter) % 2 == 0:
                x = int(new_num[i]) * 2
                if x > 9:
                    x -= 9
                total_sum += x
            else:
                total_sum += int(new_num[i])
            counter += 1

        return total_sum % 10 == 0
        
