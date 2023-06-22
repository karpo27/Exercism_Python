def recite(start_verse, end_verse):

    verse_1 = [
        "first",
        "second",
        "third",
        "fourth",
        "fifth",
        "sixth",
        "seventh",
        "eighth",
        "ninth",
        "tenth",
        "eleventh",
        "twelfth"
    ]

    verse_2 = [
        "and a Partridge in a Pear Tree.",
        "two Turtle Doves",
        "three French Hens",
        "four Calling Birds",
        "five Gold Rings",
        "six Geese-a-Laying",
        "seven Swans-a-Swimming",
        "eight Maids-a-Milking",
        "nine Ladies Dancing",
        "ten Lords-a-Leaping",
        "eleven Pipers Piping",
        "twelve Drummers Drumming"
    ]

    verse_3 = verse_2.copy()
    verse_3.reverse()

    new_verse = []
    for i in range(len(verse_1)):
        if i == 0:
            new_verse.append(f'On the {verse_1[i]} day of Christmas my true love gave to me: {verse_2[i].removeprefix("and ")}')
        else:
            new_verse.append(f'On the {verse_1[i]} day of Christmas my true love gave to me: {verse_2[i]}, {", ".join(verse_3[-i:])}')

    return new_verse[start_verse-1:end_verse]
