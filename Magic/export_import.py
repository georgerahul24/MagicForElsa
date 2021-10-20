import json

from Magic import theme, indexer


def export() -> None:
    """This function is to export the data"""
    from os import getcwd
    from tkinter import filedialog

    # see https://stackoverflow.com/questions/19476232/save-file-dialog-in-tkinter
    f = filedialog.asksaveasfile(mode="w", defaultextension=".json")
    if f is not None:
        try:
            USERNAMEPATH = getcwd() + "\\resources\\ users.elsa"
            with open(USERNAMEPATH) as usernamefile:
                username_data = json.load(usernamefile)
            json.dump({"indexfolders": indexer.read_indexer_folders(), "theme": theme.read_theme(),"usernames": f"{username_data}"}, f, indent=4)
            f.close()
            print("Successfully exported the data")
            del f, USERNAMEPATH
        except Exception as e:
            print("Some error happened", e)
    else:
        print("No file selected")


def import_data() -> None:
    """This function is to import the data"""
    try:
        from tkinter import filedialog
        from os import getcwd, remove
        initpth, indexerpth = (getcwd() + "\\resources\\ initial.elsa"), (getcwd() + "\\resources\\ indexerpaths.elsa")
        f = filedialog.askopenfile(mode="r", defaultextension=".json")
        if f is not None:
            data = json.load(f)
            indexdata, themedata, usernamedata = data.get("indexfolders"), data.get("theme"), data.get("usernames")
            if indexdata is not None:
                with open(indexerpth, "w") as indexfile:
                    json.dump(indexdata, indexfile, indent=4)
                try:
                    # To rebuilt the indexes
                    remove((getcwd() + "\\resources\\ indexer.elsa"))
                except:
                    pass
            with open(initpth, "w") as themefile:
                themefile.write(f"{themedata[0]};{themedata[1]};{themedata[2]}")
            USERNAMEPATH = getcwd() + "\\resources\\ users.elsa"
            # see https://stackoverflow.com/questions/39491420/python-jsonexpecting-property-name-enclosed-in-double-quotes
            # json doesn't allow single quotes. Only allows double qoutes
            usernamedata = json.loads(usernamedata.replace("'", '"'))
            with open(USERNAMEPATH, "w") as userfile:
                json.dump(usernamedata, userfile, indent=4)
            print("Imported usernames")
            f.close()
            del initpth, indexerpth, f, data, indexdata, themedata, usernamedata, USERNAMEPATH
    except Exception as e:
        print("Some error happened", e)
