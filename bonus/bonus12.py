# feet_inches = input("Enter feet and inches: ")
#
# def parse(feet_and_inches):
#     parts = feet_and_inches.split(" ")
#     feet = float(parts[0])
#     inches = float(parts[1])
#
#     return feet, inches
#
# def convert_meters(feet, inches):
#     meters = feet * 0.3048 + inches * 0.0254
#     return meters
#
# f, i = parse(feet_inches)
# result = convert_meters(f, i)
# print("fi", f, i)
#
# if result < 1:
#     print('Kid is too small')
# else:
#     print('kid can use the slide')


# def speed(distance, time):
#     return distance / time
#
#
# print(speed(200, 4))

def calculate_time( h, g=9.80665,):
    t = (2 * h / g) ** 0.5
    return t


time = calculate_time(100)
print(time)