def proverb(*args, qualifier):
    text = "For want of a {} the {} was lost."
    last_text = "And all for the want of a {}."
    result = []
    for i in range(len(args)):
        if i < len(args) - 1:
            result.append(text.format(args[i], args[i + 1]))
        else:
            if qualifier is None:
                result.append(last_text.format(args[0]))
            else:
                result.append(last_text.format(qualifier + " " + args[0]))

    return result
    
