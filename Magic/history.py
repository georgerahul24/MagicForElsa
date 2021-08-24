import datetime, webbrowser


def user_file(username, command, task_did):
    history = open(f'{username}.elsa', 'a')
    history.write(
        f'{datetime.datetime.now()} user input: {command}, output: {task_did}')
    history.write('\n')
    history.close()


def user_read(event="", username="admin"):

    webbrowser.open(f"{username}.elsa")


def clear_history(name):
    history = open(f'{name}.elsa', 'w')
    history.write('')
    history.close()
