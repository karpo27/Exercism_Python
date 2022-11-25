from sets_categories_data import (VEGAN,
                                  VEGETARIAN,
                                  KETO,
                                  PALEO,
                                  OMNIVORE,
                                  ALCOHOLS,
                                  SPECIAL_INGREDIENTS)


def clean_ingredients(dish_name, dish_ingredients):
    return (dish_name, set(dish_ingredients))
    

def check_drinks(drink_name, drink_ingredients):
    for i in drink_ingredients:
        if i in ALCOHOLS:
            return drink_name + " Cocktail"
      
    return drink_name + " Mocktail"


def categorize_dish(dish_name, dish_ingredients):
    vegan = 0
    vegetarian = 0
    keto = 0
    paleo = 0
    omnivore = 0
    
    for i in dish_ingredients:
        if i in VEGAN:
            vegan += 1
        if i in VEGETARIAN:
            vegetarian += 1
        if i in KETO:
            keto += 1
        if i in PALEO:
            paleo += 1
        if i in OMNIVORE:
            omnivore += 1

    comparative = [vegan, vegetarian, keto, paleo, omnivore]

    if max(comparative) == omnivore:
        return dish_name + ": OMNIVORE"
    elif max(comparative) == paleo:
        return dish_name + ": PALEO"
    elif max(comparative) == keto:
        return dish_name + ": KETO"
    elif max(comparative) == vegetarian:
        return dish_name + ": VEGETARIAN"
    else:
        return dish_name + ": VEGAN"
   
    
def tag_special_ingredients(dish):
    new_list = []
    for i in dish[1]:
        if i in SPECIAL_INGREDIENTS:
            new_list.append(i)
        
    return (dish[0], set(new_list))


def compile_ingredients(dishes):
    result = []
    for i in dishes:
        for j in i:
            result.append(j)

    return set(result)


def separate_appetizers(dishes, appetizers):
    set_dishes = set(dishes)
    join = (set(dishes)) & (set(appetizers))
    set_dishes.difference_update(join) 
    
    return set_dishes
   

def singleton_ingredients(dishes, intersection):
    new_list = []
    for i in dishes:
        for j in i:
            new_list.append(j)

    set_list = set(new_list)
    set_list.difference_update(intersection)
    
    return set_list

     
