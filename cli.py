# from functions import  functions.get_todos, functions.write_todos
# from functions import  *
from modules import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")

print("It is", now)
while True:

    user_action = input("Type add, show, edit, complete or exit: ")
    # strip the user_action
    user_action = user_action.strip()

    path = "todos.txt"

    if user_action.startswith("add"):
        todo = user_action[4:] + "\n"

        todos = functions.get_todos(path)

        todos.append(todo)

        functions.write_todos(todos, path)
    elif "show" in user_action:
        todos = functions.get_todos(path)
        # new_todos = [item.strip("\n") for item in todos]

        for index, item in enumerate(todos):
            item = item.strip("\n")
            print(f"{index + 1}. {item.title()}")
    elif "edit" in user_action:
        try:
            number = user_action[5:]
            number = int(number) -1
            todos = functions.get_todos(path)

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + "\n"

            # print(todos)

            functions.write_todos(todos, path)
        except Exception as e :
            print(e)
            print("Your command is not valid")
            continue
    elif "complete" in user_action:
        try:
            number = user_action[len("complete") + 1:]

            index = int(number) - 1

            todos = functions.get_todos(path)

            todo_to_remove = todos[index].strip("\n")
            todos.pop(index)

            functions.write_todos(todos, path)

            message = f"Todo {todo_to_remove} was removed from the list."

            print(message)
        except IndexError:
            print("There is no item with that number")
            continue
    elif "exit" in user_action:
        break
    else:
        print("Command is not valid")

print("Bye")
