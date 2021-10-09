import datetime
import os
import webbrowser
from pathlib import Path


def user_file(username: str, command: str, task_did: str):
    """[Used to save the history of the user]
    """
    userpth = os.getcwd() + f"\\resources\\ {username}.elsa"
    with open(userpth, "a") as history:
        history.write(f"""
            ---------------------------------------------------------------------
            DATE{datetime.datetime.now()} USER INPUT: {command} OUTPUT: {task_did}"""
                      )
        history.write("\n")
        del history


def user_read(event="", username: str = "dummy"):
    """[Open the user history file]

    Args:
        event (str, optional): [Not imp]. Defaults to "".
        username (str, optional): [Name of the user to be opened]. Defaults to "admin".
    """
    userpth = os.getcwd() + f"\\resources\\ {username}.elsa"

    if not Path(userpth).exists():
        userpth = os.getcwd() + "\\resources\\ dummy.elsa"
    webbrowser.open(userpth)


def clear_history(name: str):
    """[Clears the history of the user]

    Args:
        name ([str]): [Name of the user to clear]
    """
    userpth = os.getcwd() + f"\\resources\\ {name}.elsa"
    with open(userpth, "w") as history:
        history.write("")
        del history
