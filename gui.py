import functions
import FreeSimpleGUI as sg
import time

clock = sg.Text('')
label  = sg.Text('Enter Todo')
text_input =  sg.Input(key='todo')
add_button = sg.Button('Add', bind_return_key=True)
list_box = sg.Listbox(values=functions.get_todos(), key='todos',
                      enable_events=True, size=(45, 10))
edit_button = sg.Button('Edit')
complete_button = sg.Button('Complete')
exit_button = sg.Button('Exit')

layout =  [
    [label],
    [text_input, add_button],
    [list_box, edit_button, complete_button],
    [exit_button]
]

window = sg.Window('My Todo App', layout, font=("Helvetica", 20))

while True:
    event, values = window.read()
    # print(event)
    # print(values)

    match event:
        case 'Add':
            todos = functions.get_todos()
            new_todo = values['todo'].strip()
            if not new_todo:
                sg.popup("Todo cannot be empty.", title="Input Error")
                continue
            todos.append(new_todo  + '\n')
            functions.write_todos(todos)
            window['todo'].update('')
            window['todos'].update(values=todos)
        case 'Edit':
            try:
                todo = values['todos'][0]
                ''' window['todo'].update(todo)'''
                new_todo = values['todo'].strip()
                todos = functions.get_todos()
                index = todos.index(todo)
                todos[index] = new_todo + '\n'
                functions.write_todos(todos)
                window['todo'].update('')
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Select an item to edit.", title="Input Error", font=("Helvetica", 20))
        case 'todos':
            x = values['todos'][0].strip('\n') # this value will be rendered on input
            window['todo'].update(x)

        case 'Complete':
            try:
                todo_to_complete = values['todos'][0] # this is the case todos value
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todo'].update('')
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Todo cannot be empty.", title="Input Error", font=("Helvetica", 20))
        case 'Exit':
            break
        case sg.WIN_CLOSED:
            break
print('Bye')
window.close()