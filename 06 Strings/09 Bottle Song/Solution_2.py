def recite(start, take=1):
    pattern = [
        "{0} green {1} hanging on the wall,",
        "{0} green {1} hanging on the wall,",
        "And if one green bottle should accidentally fall,",
        "There'll be {0} green {1} hanging on the wall."
    ]
    num_dict = {
        0: "no", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine",
        10: "ten"
    }
    song = []
    for i in range(take):
        for j, lyric in enumerate(pattern):
            if j in [0, 1]:
                song.append(lyric.format(num_dict[start].capitalize(), "bottle" if start <= 1 else "bottles"))
            elif j == 3:
                song.append(lyric.format(num_dict[start - 1], "bottle" if start - 1 == 1 else "bottles"))
            else:
                song.append(lyric)
        start -= 1
        if i != take - 1:
            song.append("")

    return song
  
