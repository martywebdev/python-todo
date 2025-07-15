import FreeSimpleGUI as sg
import zipfile

"""Backend"""

def extract_archive(archive_path, destination):
    with zipfile.ZipFile(archive_path, 'r') as archive:
        archive.extractall(destination)

sg.theme("Black")

label1 = sg.Text("Select Archive")
input1 = sg.Input()
choose_button1 = sg.FileBrowse("Choose", key="archive")

label2 = sg.Text("Select Destination")
input2 = sg.Input()
choose_button2 = sg.FolderBrowse("Choose", key="folder")

extract_button = sg.Button('Extract')
output_label = sg.Text(key="output", text_color="green")

window = sg.Window(title="Extractor", layout=[
    [label1, input1, choose_button1],
    [label2, input2, choose_button2],
    [extract_button, output_label]
])


while True:
    event, values = window.read()
    archive = values['archive']
    folder = values['folder']

    extract_archive(archive, folder)
    window['output'].update("Extract Success")

window.close()