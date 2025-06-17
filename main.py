todos = [] 

while True:
    user_text = input('Enter todo: ')

    if user_text == 'quit':
        break
    else:
        todos.append(user_text)

    print(todos)
