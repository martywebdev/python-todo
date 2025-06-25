todos = ['eat', 'code', 'test']

while True:
    user_action = input("Type add, show, edit or exit: ")

    # strip the user_action
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input('Enter a todo: ')
            todos.append(todo)
        case 'show':
            # print(*todos, sep="\n")
            for index, item in enumerate(todos):
                print(f'{index + 1}. {item.title()}')
        case 'edit':
            number = int(input("Number of the todo to edit: ")) - 1
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo
        case 'exit':
            break
        case _:
            print("Entered an unknown command")

print("Bye")