import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import WIN_CLOSED
import login, error
def validate(window, values):
    username = values['username']
    password = values['password']
    fruit = values['fruit']
    result = ''

    # reset message
    error.displayMessages(window)

    # -------------------------------- validate username, password and favourite fruit-------------------------------------
    if username == 'user2':
        result = 'Failed'
        err_msg = ['Register Failed','-Duplicate Username']
        error.displayMessages(window,err_msg)

    if username == '' or password == '' or fruit == '':
        result = 'Failed'
        err_msg = ['Register Failed','-Can\'t leave anything blank!']
        error.displayMessages(window,err_msg)

    if fruit.lower() == 'apple' or fruit.lower() == 'apples':
        result = 'Failed'
        err_msg = ['Register Failed','-What apples?!']
        error.displayMessages(window,err_msg)

    return result

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
                    [sg.Button('Back'),sg.Button('Submit')],
                    [sg.Text(k='messages',size=(50,3))]
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
            result = validate(window, values)

            if not 'Failed' == result:
                # go to login window
                window.close()
                login.window()


    window.close()
