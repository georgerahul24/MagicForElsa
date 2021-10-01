import json
import os
import pathlib
import time

from talk1.talk1 import talk

from Magic import license, theme


@license.licence_window
def install_files():
    print("Licence accepted")
    try:
        """[Installs the neccessary files for Elsa to work]"""
        # Making a relative folder called resources
        folderpath = os.getcwd() + "\\resources"
        folderpath = pathlib.Path(folderpath)
        if not os.path.exists(folderpath):
            os.makedirs(folderpath)
        dummytpth = os.getcwd() + "\\resources\\ dummy.elsa"
        with open(dummytpth, "w") as f:
            f.write(
                "Hey!The file you are looking is not found.Try again later")
        # Writing the default theme
        initpth = os.getcwd() + "\\resources\\ initial.elsa"
        with open(initpth, "w") as f:
            f.write(
                "black;purple;light green\n#The order is bg,font color,button colour\n#Please remember to use ';' to separate colours :D"
            )
        indexerpth = os.getcwd() + '\\resources\\ indexerpaths.elsa'
        f = open(indexerpth, "w")
        f.close()
        # writing the users folder with default user admin and default password 1234
        userpth = os.getcwd() + "\\resources\\ users.elsa"
        with open(userpth, "w") as f:
            talk("Hey new user. Let us get started")
            talk("Please create an account to proceed")
            from Magic import usergui
            try:
                initusr, initpsswd = usergui.user_page_init()
            except:
                initusr = "admin"
                initpsswd = "1234"
            json.dump({initusr: initpsswd}, f, indent=4)
        talk("Now let us select a new theme")
        theme.theme_selector()
        print("added file 'initial.Elsa'")
    except Exception as e:
        talk("Sorry some error happened. Please try again")
        print(e)
        time.sleep(4)
        exit()
