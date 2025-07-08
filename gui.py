import functions
import FreeSimpleGUI as sg

label  = sg.Text('Enter Todo')
text_input =  sg.Input(key='-INPUT-')
add_button = sg.Button('Add')

layout =  [[label], [text_input, add_button]]

window = sg.Window('My Todo App', layout)

window.read()
window.close()