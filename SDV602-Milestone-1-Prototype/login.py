import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import WIN_CLOSED
import register, app

def window():
    """
        The login window.
    """

    result = ''
    messages = ()

    layout = [  [sg.Text('The World\'s Leading \n(actually not..) \nData Explorer Screen', size=(30, 3), justification='center', font=("Helvetica", 25))],
                [sg.Column([
                    [sg.Text('Username')],
                    [sg.Input(key='username')],
                    [sg.Text('Password')],
                    [sg.Input(key='password')],
                    [sg.Button('Register'),
                    sg.Button('Login')],
                    [sg.Text(k='results_messages')]
                    ],justification='c')
                ]
              ]

    window = sg.Window('World Leading.. DES', layout)

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            break

        if event == 'Register':
            window.close()
            
            # Go to register window
            register.window()
            
        if event == 'Login':
            window.close()
            
            # if true, go to main app 
            app.main()

            # if false, display the error message

    window.close()


if __name__ == "__main__":
    window()