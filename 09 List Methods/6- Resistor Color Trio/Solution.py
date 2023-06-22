def label(colors):
    resistor_code = {
        "black": "0",
        "brown": "1",
        "red": "2",
        "orange": "3",
        "yellow": "4",
        "green": "5",
        "blue": "6",
        "violet": "7",
        "grey": "8",
        "white": "9"
    }

    res_value = ""
    for i in range(len(colors)):
        if colors[i] in resistor_code:
            if i <= 1:
                res_value += resistor_code[colors[i]]
            else:
                res_value += "0" * int(resistor_code[colors[i]])

    res_value_alt = ""
    if int(res_value) < 1000:
        res_value_alt += res_value + " ohms"
    elif 1000 <= int(res_value) < 1000000:
        res_value_alt += str(round(int(res_value) / 1000)) + " kiloohms"

    return res_value_alt
    
