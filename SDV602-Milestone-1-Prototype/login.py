import PySimpleGUI as sg

result = ''
messages = []



if __name__ == "__main__":
    
    def make_login_layout():
            
        layout = [[sg.Text("The World's Leading (actually not..) \nData Explorer Screen")],
                [sg.Input('Username', key='username')],
                [sg.Input('Password', key='password')],
                [sg.Button('register', key='register'), sg.Button('Login', key='Login')],
                [sg.Text(f'{result}\n{messages}')]]

        return layout
    

