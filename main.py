while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    # strip the user_action
    user_action = user_action.strip()


    if 'add' in user_action  or 'new' in user_action:
        todo = user_action[4:] + '\n'
        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        todos.append(todo)

        with open('todos.txt', 'w') as file:
            file.writelines(todos)
    elif 'show' in user_action:
        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        # new_todos = [item.strip('\n') for item in todos]

        for index, item in enumerate(todos):
            item = item.strip('\n')
            print(f'{index + 1}. {item.title()}')
    elif 'edit' in user_action:

        number = user_action[5:]
        number = int(number) -1
        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        new_todo = input("Enter new todo: ")
        todos[number] = new_todo + '\n'

        # print(todos)

        with open('todos.txt', 'w') as file:
            file.writelines(todos)
    elif 'complete' in user_action:

        number = user_action[len('complete') + 1:]

        number = int(number) - 1

        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        index = number - 1
        todo_to_remove = todos[index].strip('\n')
        todos.pop(index)

        with open('todos.txt', 'w') as file:
            file.writelines(todos)

        message = f"Todo {todo_to_remove} was removed from the list."

        print(message)
    elif 'exit' in user_action:
        break
    # elif _:
    #     print("Entered an unknown command")
    else:
        print('Command is not valid')

print("Bye")