import FreeSimpleGUI as sg

label1 = sg.Text('Select files to compress: ')
input1 = sg.Input()
choose_button1 = sg.FolderBrowse("Choose") #file open button

label2 = sg.Text('Select destination folder: ')
input2 = sg.Input()
choose_button2 = sg.FolderBrowse("Choose") #file open button

compress_button  = sg.Button("Convert")
layout = [[label1, input1, choose_button1],[label2, input2, choose_button2], [compress_button]]
window = sg.Window("Files Compressor", layout=layout)
window.read()
window.close()