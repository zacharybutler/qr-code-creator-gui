import PySimpleGUI as sg
from qrcreator.qrcode_generator import create_qr

sg.theme('LightGrey1')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Column([[sg.Image('qrcreator/images/harambe.png')]], justification="center")],
            [sg.Text('Link:', font=600, size=(6, 1)), sg.InputText(key="-LINK-", font=600)],
            [sg.Text('Save As:', font=600, size=(6, 1)), sg.InputText(key="-NAME-", font=600)],
            [sg. Text('Save At:', font=600, size=(6, 1)), sg.Input(key="-FOLDER-", enable_events=True, font=600), sg.FolderBrowse()],
            [sg.Button('Submit'), sg.Button('Cancel')]
        ]

# Create the Window
window = sg.Window('Harambe QR Creator', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event in [sg.WIN_CLOSED, 'Cancel']: # if user closes window or clicks cancel
        break
    elif event == "Submit":
        create_qr(values["-LINK-"], values["-NAME-"], values["-FOLDER-"])

window.close()