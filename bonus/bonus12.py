# feet_inches = input("Enter feet and inches: ")
#
# def convert_meters(feet_inches):
#     parts = feet_inches.split(" ")
#     feet = float(parts[0])
#     inches = float(parts[1])
#
#     meters = feet * 0.3048 + inches * 0.0254
#     return meters
#
# result = convert_meters(feet_inches)
#
# if result < 1:
#     print('Kid is too small')
# else:
#     print('kid can use the slide')


def speed(distance, time):
    return distance / time


print(speed(200, 4))