def is_criticality_balanced(temperature, neutrons_emitted):
    return temperature < 800 and neutrons_emitted > 500 and temperature * neutrons_emitted < 500000

def reactor_efficiency(voltage, current, theoretical_max_power):
    generated_power = voltage * current
    efficency_band = (generated_power / theoretical_max_power) * 100
    if efficency_band >= 80:
        return "green"
    elif 60 <= efficency_band < 80:
        return "orange"
    elif 30 <= efficency_band < 60:
        return "red"
    else:
        return "black"
    
def fail_safe(temperature, neutrons_produced_per_second, threshold):
    temp = temperature * neutrons_produced_per_second
    if temp < 0.9 * threshold:
        return "LOW"
    elif 0.9 * threshold < temp < 1.1 * threshold:
        return "NORMAL"
    else:
        return "DANGER"
