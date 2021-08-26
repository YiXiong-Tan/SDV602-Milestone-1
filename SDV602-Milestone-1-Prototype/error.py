def displayMessages(window,messages=['']):
    
    # update messages text
    message_in_line = ''
    for msg in messages:
        message_in_line += '\n'+msg

    window['messages'].update(f'{message_in_line}')
