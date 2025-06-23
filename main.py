todos = []

while True:
    user_action = input("Type add, show or exit: ")

    # strip the user_action
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input('Enter a todo: ')
            todos.append(todo)
        case 'show':
            # print(*todos, sep="\n")
            for item in todos:
                print(item.title())
        case 'exit':
            break
        case _:
            print("Entered an unknown command")

print("Bye")