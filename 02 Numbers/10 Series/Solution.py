def slices(series, length):
    if length < 0:
        raise ValueError("slice length cannot be negative")
    elif length == 0:
        raise ValueError("slice length cannot be zero")

    if not series:
        raise ValueError("series cannot be empty")

    if len(series) < length:
        raise ValueError("slice length cannot be greater than series length")

    substring = []
    i = 0
    while i < len(series) - length + 1:
        substring.append(series[i:length + i])
        i += 1

    return substring
  
