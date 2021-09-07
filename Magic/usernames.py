"""Created by George Rahul
Calls the login page and verifies the username and password entered"""

from Magic.GUI import SecurityUI
from talk1.talk1 import talk
from Magic import file_database


def verify_usernames():

    return False


def check_user():
    """[Security process]"""
    try:
        # initialise the security variable
        check_user.security = verify_usernames()
        # .....accept the username and password.......
        talk("Please enter the username and password")
        # ...running GUI.py............
        username, password = SecurityUI()
        # verifying with database

        if password == file_database.check_user_from_file(username):
            check_user.security = True
        else:
            check_user.security = False

        check_user.loginname = username
        del username,password

    except Exception as e:
        print(e)
        check_user.security = False
