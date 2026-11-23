def percentage(part, total):
    if total == 0:
        raise ValueError("Total cannot be zero")

    return (part / total) * 100

def percentage_change(old, new):
    if old == 0:
        raise ValueError("Old value cannot be zero")

    return ((new - old) / old) * 100

def calculate_rate(quantity, time):
    if time == 0:
        raise ValueError("Time cannot be zero")

    return quantity / time