def get_todos(file_path = 'todos.txt'):
    with open(file_path, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_list, file_path = 'todos.txt'):
    with open(file_path, 'w') as file_local:
        file_local.writelines(todos_list)


while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    # strip the user_action
    user_action = user_action.strip()

    path = "todos.txt"

    if user_action.startswith('add'):
        todo = user_action[4:] + '\n'

        todos = get_todos(path)

        todos.append(todo)

        write_todos(todos, path)
    elif 'show' in user_action:
        todos = get_todos(path)
        # new_todos = [item.strip('\n') for item in todos]

        for index, item in enumerate(todos):
            item = item.strip('\n')
            print(f'{index + 1}. {item.title()}')
    elif 'edit' in user_action:
        try:
            number = user_action[5:]
            number = int(number) -1
            todos = get_todos(path)

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'

            # print(todos)

            write_todos(todos, path)
        except Exception as e :
            print(e)
            print("Your command is not valid")
            continue
    elif 'complete' in user_action:
        try:
            number = user_action[len('complete') + 1:]

            index = int(number) - 1

            todos = get_todos(path)

            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            write_todos(todos, path)

            message = f"Todo {todo_to_remove} was removed from the list."

            print(message)
        except IndexError:
            print('There is no item with that number')
            continue
    elif 'exit' in user_action:
        break
    else:
        print('Command is not valid')

print("Bye")