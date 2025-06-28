prompt = input("Enter a new member: ")

with open("members.txt", "a+") as file:
    file.seek(0)  # Move to beginning to read
    existing_members = file.readlines()

    if prompt + '\n' not in existing_members:
        file.write(prompt + '\n')
