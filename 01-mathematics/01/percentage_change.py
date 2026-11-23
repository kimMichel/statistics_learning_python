def percentage_change(old, new):
    if old == 0:
        raise ValueError("Old value cannot be zero")

    return ((new - old) / old) * 100

print(percentage_change(200, 150))

print(percentage_change(150, 200))