def response(hey_bob):
    if hey_bob.count("?") > 0 and hey_bob.isupper() == False and (hey_bob.index("?") + 1) == len(hey_bob) or hey_bob.count("?") > 0 and hey_bob.isupper() == False and hey_bob[len(hey_bob) - 1] == " ":
        return "Sure."
    elif hey_bob.count("?") == 0 and hey_bob.isupper() == True:
        return "Whoa, chill out!"
    elif hey_bob.count("?") > 0 and hey_bob.isupper() == True:
        return "Calm down, I know what I'm doing!"
    elif hey_bob.count("?") == 0 and hey_bob.isupper() == False and hey_bob.count(" ") == len(hey_bob) or hey_bob.count("?") == 0 and hey_bob.isupper() == False and hey_bob == "" or hey_bob.count("?") == 0 and hey_bob.isupper() == False and hey_bob[0] == " " and hey_bob[1] != " " or hey_bob.count("?") == 0 and hey_bob.isupper() == False and "\t" in hey_bob:
        return "Fine. Be that way!"
    else:
        return "Whatever."
