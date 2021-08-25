import datetime, webbrowser,os


def user_file(username, command, task_did):
    userpth = os.getcwd() + f'\\resources\\ {username}.elsa'
    history = open(userpth, 'a')
    history.write(
        f'{datetime.datetime.now()} user input: {command}, output: {task_did}')
    history.write('\n')
    history.close()


def user_read(event="", username="admin"):
    userpth = os.getcwd() + f'\\resources\\ {username}.elsa'
    webbrowser.open(userpth)


def clear_history(name):
    userpth = os.getcwd() + f'\\resources\\ {name}.elsa'
    history = open(userpth, 'w')
    history.write('')
    history.close()
