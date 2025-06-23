

todos = []

while True:
    print(f"Select option\n[1] view todos\n[2] add todo")

    try:
        user_input = input('Enter option: ')
        if user_input == 'quit':
            break

        user_option = int(user_input)

        if user_option == 1:
            print("Your Todos:")
            for todo in todos:
                print(f"- {todo}")
        elif user_option == 2:
            todo = input("Enter todo: ")
            todos.append(todo)
        else:
            print("Invalid option. Choose 1 or 2.")

    except ValueError:
        print("Please enter a valid number (1 or 2) or type 'quit' to exit.")
