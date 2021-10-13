"""This module deals with adding and verifying usernames"""
import gc
import json
import os

# Get the path of users.elsa
userpth = os.getcwd() + "\\resources\\ users.elsa"


def check_user_from_file(username: str)->str:
    """[This extension is used to check if the user is valid or not ]
    Note:Returns None if no such user is found else the password is returned
"""
    try:

        with open(userpth, "r") as file:
            data = json.load(file)
            part2 = data.get(username, None)
        return part2

    except Exception as e:
        print("It seems that some error has happened", e)
        del e


def write_to_file(username: str, password: str)->int:
    """[Writes the username and password to users.elsa file]
    Returns:
        [int]: [1 if it is a success and -1 if the process is a failure]
    """
    try:

        with open(userpth, "r") as file:
            data = json.load(file)
            print(file)

        if len(username) != 0 and username not in [
            "initial",
            "cache",
            "users",
            "user",
            "theme",
            "indexer",
            "resources",
            "dummy",
            "indexerpaths",
            "indexerfolder",
        ]:
            with open(userpth, "w") as file:
                data[username] = password
                json.dump(data, file, indent=4)
            print(f"Added user {username} ")
            # returns state = 1 so that program knows that writing was succesful
            del file, username, password, data
            gc.collect()
            return 1

        else:
            print("User already exists")
            # return state = -1 to know that user wasnt added successfully due to username repetitions,empty username,username conflicts,etc
            return -1
    except Exception as e:
        print(e, "Try again")
