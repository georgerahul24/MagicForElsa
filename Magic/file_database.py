"""This module deals with adding and verifying usernames"""
import gc
import os
import json

# Get the path of users.elsa
userpth = os.getcwd() + "\\resources\\ users.elsa"

def check_user_from_file(username):
    """[This extension is used to check if the user is vaid or not ]

    Args:
        username ([str]): [Username to search]

    Returns:
        [str]: [Returns the passwprd of user if found]
    """
    try:

        with open(userpth, "r") as file:
            data = json.load(file)
            part2 = data.get(username, None)
        return part2

    except Exception as e:
        print("It seems that some error has happened", e)
        del e


def write_to_file(username, password):
    """[Writes the username and password to users.elsa file]

    Args:
        username ([str]): [Username to be added]
        password ([str]): [Password to be added]

    Returns:
        [int]: [1 if it is a success and -1 if the process is a failure]
    """
    try:

        with open(userpth, "r") as file:
            data = json.load(file)
            print(file)
        file = open(userpth, "w")
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
        ]:

            data[username] = password
            json.dump(data, file)
            file.close()
            print(f"Added user {username} ")
            # returns state = 1 so that program knows that writing was succesful
            del file,username,password,data
            gc.collect()
            return 1

        else:
            print("User already exists")
            # return state = -1 to know that user wasnt added successfully due to username repetitions,empty username,username conflicts,etc
            return -1
    except Exception as e:
        print(e, "Try again")
