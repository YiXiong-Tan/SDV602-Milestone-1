import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import WIN_CLOSED
import login

def window():
    """
    The register window.
    There will be a few validations happening here.
    - duplicate username
    - if the favourite fruit answer is too simple
    """
    result = ''
    messages = list()

    layout = [[sg.Text('Register', size=(30, 1), justification='center', font=("Helvetica", 25))],
                [sg.Column([
                    [sg.Text('Username')],
                    [sg.Input(key='username')],
                    [sg.Text('Password')],
                    [sg.Input(key='password')],
                    [sg.Text('What\'s your favourite fruit?')],
                    [sg.Input(key='fruit')],
                    [sg.Button('Back'),
                    sg.Button('Submit')],
                    [sg.Text(k='results_messages')]
                    ], justification='c')
                ]
              ]

    window = sg.Window('DES', layout)

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            break

        if event == 'Back':
            window.close()

            # Back to login window
            login.window()

        if event == 'Submit':
            # validate registration
            
            # if good, go to login window
            window.close()
            login.window()

            # if false, display the error message

    window.close()
