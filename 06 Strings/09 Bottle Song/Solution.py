def recite(start, take=1):
    pattern = [
        "X green bottles hanging on the wall,",
        "X green bottles hanging on the wall,",
        "And if one green bottle should accidentally fall,",
        "There'll be X green bottles hanging on the wall."
    ]
    num_dict = {
        0: "no", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten"
    }
    song = []
    for i in range(take):
        for j, lyric in enumerate(pattern):
            if j in [0, 1]:
                if start <= 1:
                    temp = lyric.replace("bottles", "bottle")
                    temp = temp.replace("X", num_dict[start].capitalize())
                else:
                    temp = lyric.replace("X", num_dict[start].capitalize())
                song.append(temp)
            elif j == 3:
                if start - 1 == 1:
                    temp = lyric.replace("bottles", "bottle")
                    temp = temp.replace("X", num_dict[start - 1])
                else:
                    temp = lyric.replace("X", num_dict[start - 1])
                song.append(temp)
            else:
                song.append(lyric)
        start -= 1
        if i != take - 1:
            song.append("")

    return song
