import json
import os
import pathlib
import time
from Magic import add_user, theme, license
from talk1.talk1 import talk


def install_files():
    # Show the lisence window
    license.licence_window()
    try:
        """[Installs the neccessary files for Elsa to work]"""
        # Making a relative folder called resources
        folderpath = os.getcwd() + "\\resources"
        folderpath = pathlib.Path(folderpath)
        if not os.path.exists(folderpath):
            os.makedirs(folderpath)
        dummytpth = os.getcwd() + "\\resources\\ dummy.elsa"
        f = open(dummytpth, "w")
        f.write("Hey!The file you are looking is not found.Try again later")
        f.close()
        # Writing the default theme
        initpth = os.getcwd() + "\\resources\\ initial.elsa"
        f = open(initpth, "w")
        f.write(
            "black;purple;light green\n#The order is bg,font color,button colour\n#Please remember to use ';' to separate colours :D"
        )
        f.close()
        indexerpth = os.getcwd() + f"\\resources\\ indexerpaths.elsa"
        f = open(indexerpth, "w")
        f.close()
        # writing the users folder with default user admin and default password 1234
        userpth = os.getcwd() + "\\resources\\ users.elsa"
        f = open(userpth, "w")
        talk("Hey new user. Let us get started")
        talk("Please create an account to proceed")
        try:
            initusr, initpsswd = add_user.user_page_init()
        except:
            initusr = "admin"
            initpsswd = "1234"
        json.dump({initusr: initpsswd}, f)
        f.close()
        talk("Now let us select a new theme")
        theme.theme_selector()
        print("added file 'initial.Elsa'")
    except Exception as e:
        talk("Sorry some error happened. Please try again")
        print(e)
        time.sleep(4)
        exit()
