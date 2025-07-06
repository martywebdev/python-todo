# from bonus.parser12 import parse
from converter12 import convert_meters
from parser12 import parse

feet_inches = input("Enter feet and inches: ")

f, i = parse(feet_inches)
result = convert_meters(f, i)
print("fi", f, i)

if result < 1:
    print('Kid is too small')
else:
    print('kid can use the slide')


def speed(distance, time):
    return distance / time


print(speed(200, 4))

# def calculate_time( h, g=9.80665,):
#     t = (2 * h / g) ** 0.5
#     return t
#
#
# time = calculate_time(100)
# print(time)