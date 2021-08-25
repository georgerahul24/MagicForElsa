import json
import os
import pathlib


def install_files():
    """[Installs the neccessary files for Elsa to work]
    """
    #Making a relative folder called resources
    folderpath = os.getcwd() + '\\resources'
    folderpath = pathlib.Path(folderpath)
    if not os.path.exists(folderpath):
        os.makedirs(folderpath)
    # Writing the default theme
    initpth = os.getcwd() + '\\resources\\ initial.elsa'
    f = open(initpth, 'w')
    f.write(
        "black;purple;light green\n#The order is bg,font color,button colour\n#Please remember to use ';' to separate colours :D"
    )
    f.close()

    # writing the users folder with default user admin and default password 1234
    userpth = os.getcwd() + "\\resources\\ users.elsa"
    f = open(userpth, 'w')
    json.dump({'admin': "1234"}, f)
    f.close()
    print("added file 'initial.Elsa'")
