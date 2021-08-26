import home

def main(credentials):
    """
    The purpose of main is to perform some validation tasks before going to the home page.
    """
    try:
        home.window(credentials)
    except ValueError:
        print(ValueError)
