def create_inventory(items):
    alt_items = list(set(items))
    dictionary = {}
    for i in range(len(alt_items)):
        for j in range(len(items)):
            if alt_items[i] == items[j]:
                dictionary[items[j]] = items.count(items[j])

    return dictionary
    
def add_items(inventory, items):
    alt_items = list(set(items))
    dictionary = {}
    for i in range(len(alt_items)):
        for j in range(len(items)):
            if alt_items[i] == items[j]:
                dictionary[items[j]] = items.count(items[j])

    if len(inventory) == 0:
        return dictionary
    
    new_inventory = {}
    for x, y in inventory.items():
        for i, j in dictionary.items():
            if i == x:
                new_inventory.update({x: y + j})
            elif i not in inventory:
                new_inventory.update({i: j})
            elif x not in dictionary:
                new_inventory.update({x: y})

    return new_inventory

def decrement_items(inventory, items):
    alt_items = list(set(items))
    dictionary = {}
    for i in range(len(alt_items)):
        for j in range(len(items)):
            if alt_items[i] == items[j]:
                dictionary[items[j]] = items.count(items[j])

    new_inventory = {}
    for x, y in inventory.items():
        for i, j in dictionary.items():
            if i == x:
                if y - j >= 0:
                    new_inventory.update({x: y - j})
                else:
                    new_inventory.update({x: 0})
            elif x not in dictionary:
                new_inventory.update({x: y})

    return new_inventory

def remove_item(inventory, item):
    new_inventory = {}
    for i, j in inventory.items():
        if i != item:
            new_inventory.update({i: j})

    return new_inventory 

def list_inventory(inventory):
    new_list = []
    for i, j in inventory.items():
        if j > 0:
            new_list.append((i, j))

    return new_list
    
