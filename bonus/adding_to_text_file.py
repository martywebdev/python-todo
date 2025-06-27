prompt = input("Enter a new member: ")

file = open("members.txt", 'r')
existing_members = file.readlines()
file.close()

existing_members.append(prompt + '\n')

file = open("members.txt", "w")
existing_members = file.writelines(existing_members)

file.close()