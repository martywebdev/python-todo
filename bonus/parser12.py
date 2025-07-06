def parse(feet_and_inches):
    parts = feet_and_inches.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])

    return feet, inches
