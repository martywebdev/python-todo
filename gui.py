import functions
import FreeSimpleGUI as sg

label  = sg.Text('Enter Todo')
text_input =  sg.Input(key='todo')
add_button = sg.Button('Add', bind_return_key=True)

layout =  [
    [label],
    [text_input, add_button]
]

window = sg.Window('My Todo App', layout, font=("Helvetica", 20))

while True:
    event, values = window.read()
    print(event)
    print(values)

    match event:
        case 'Add':
            todos = functions.get_todos()
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todo'].update('')
        case sg.WIN_CLOSED:
            break
window.close()