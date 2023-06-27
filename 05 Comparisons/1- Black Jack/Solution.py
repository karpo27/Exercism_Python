def value_of_card(card, A_value=1):
    if card in ['K', 'Q', 'J']:
        return 10
    elif card == 'A':
        return A_value
    else:
        return int(card)
    
def higher_card(card_one, card_two):
    value_card_one = value_of_card(card_one)
    value_card_two = value_of_card(card_two)
        
    if value_card_one > value_card_two:
        return card_one
    elif value_card_one == value_card_two:
        return card_one, card_two
    else:
        return card_two
    
def value_of_ace(card_one, card_two):
    value_card_one = value_of_card(card_one, 11)
    value_card_two = value_of_card(card_two, 11)
    
    if 21 - (value_card_one + value_card_two) < 11:
        return 1
    else:
        return 11

def is_blackjack(card_one, card_two):
    value_card_one = value_of_card(card_one, 11)
    value_card_two = value_of_card(card_two, 11)
    
    return value_card_one + value_card_two == 21
    
def can_split_pairs(card_one, card_two):
    value_card_one = value_of_card(card_one, 11)
    value_card_two = value_of_card(card_two, 11)

    return value_card_one == value_card_two
    
def can_double_down(card_one, card_two):
    value_card_one = value_of_card(card_one)
    value_card_two = value_of_card(card_two)
    
    return 9 <= value_card_one + value_card_two < 12
    
