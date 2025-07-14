import FreeSimpleGUI as sg
from zip_creator import  make_archive

label1 = sg.Text('Select files to compress: ')
input1 = sg.Input()
choose_button1 = sg.FilesBrowse("Choose", key="files") #file open button

label2 = sg.Text('Select destination folder: ')
input2 = sg.Input()
choose_button2 = sg.FolderBrowse("Choose", key="folder") #file open button

compress_button  = sg.Button("Convert")
output = sg.Text(key="output")
layout = [[label1, input1, choose_button1],[label2, input2, choose_button2], [compress_button, output]]
window = sg.Window("Files Compressor", layout=layout)

while True:
    event, values = window.read()
    filepaths = values['files'].split(";")
    folder = values["folder"]

    make_archive(filepaths, folder)

    window["output"].update("Compression completed")

window.close()