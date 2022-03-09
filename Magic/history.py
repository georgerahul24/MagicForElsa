import datetime, os, webbrowser
from pathlib import Path

currentuser = ''


def user_file(command: str, task_did: str, username = None) -> None:
    """[Used to save the history of the user]"""
    maxlength = 100
    username = currentuser if username is None else username
    with open(f"{os.getcwd()}/resources/ {username}.elsa", "a") as history:
        history.write(f"{'-' * maxlength}\n DATE{datetime.datetime.now()} USER INPUT: {command} OUTPUT: {task_did}\n{'-' * maxlength}\n\n")


def user_read(event = "", username: str = "dummy") -> None:
    """[Open the user history file]"""
    if not Path(userpth := f"{os.getcwd()}/resources/ {username}.elsa").exists():
        userpth = f'{os.getcwd()}/resources/ dummy.elsa'
    webbrowser.open(userpth)


def clear_history(name: str) -> None:
    """[Clears the history of the user]"""
    with open(f"{os.getcwd()}/resources/ {name}.elsa", "w") as history: history.write("")
