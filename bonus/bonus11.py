def get_average(file_path):
    with open(file_path, 'r') as file:
        data = file.readlines()
    values = data[1:]
    values = [float(num) for num in values]

    avg = sum(values) / len(values)
    return avg

average = get_average("files/data.txt")
print(average)


def get_maximum():
    celsius = [14, 15.1, 12.3]
    maximum = max(celsius)
    return maximum


celsius = get_maximum()
fahrenheit = celsius * 1.8 + 32

print(fahrenheit)