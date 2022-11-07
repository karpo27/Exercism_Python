def recite(start_verse, end_verse):

    verse_1 = [
        "the house that Jack built.",
        "the malt",
        "the rat",
        "the cat",
        "the dog",
        "the cow with the crumpled horn",
        "the maiden all forlorn",
        "the man all tattered and torn",
        "the priest all shaven and shorn",
        "the rooster that crowed in the morn",
        "the farmer sowing his corn",
        "the horse and the hound and the horn"
    ]

    verse_2 = [
        "lay in",
        "ate",
        "killed",
        "worried",
        "tossed",
        "milked",
        "kissed",
        "married",
        "woke",
        "kept",
        "belonged to"
    ]

    new_verse = []
    for i in range(len(verse_1)):
        if i == 0:
            new_verse.append(f'This is {verse_1[i]}')
        else:
            new_verse.append(f'This is {verse_1[i]} that {verse_2[i - 1]} {new_verse[i - 1].removeprefix("This is ")}')

    return new_verse[start_verse -1:end_verse]
    
