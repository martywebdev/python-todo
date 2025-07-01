password = input("Enter new password: ")
result = {}


# if len(password) >= 8:
#     result.append(True)
# else:
#     result.append(False)

# result.append(len(password) >= 8)
result['length'] = len(password) >= 8
digit = False
for i in password:
    if i.isdigit():
        digit = True
#
# result.append(digit)
result['isdigit'] = digit

uppercase = False
for i in password:
    if i.isupper():
        uppercase = True
result['isupper'] = uppercase
# result.append(uppercase)

print("Strong password" if all(result.values()) else "Weak password")


print(result.values())