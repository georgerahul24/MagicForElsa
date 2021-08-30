import json
from Magic import theme, indexer


def export():
    from os import getcwd
    from tkinter import filedialog
    # see https://stackoverflow.com/questions/19476232/save-file-dialog-in-tkinter
    f = filedialog.asksaveasfile(mode='w', defaultextension=".json")
    print('Starting to save file in', f)
    # theme
    themedata = theme.read_theme()

    # indexer
    indexerdata = indexer.read_indexer_folders()
    if indexerdata is None:
        indexerdata = None

    USERNAMEPATH = getcwd() + f"\\resources\\ users.elsa"
    with open(USERNAMEPATH) as usernamefile:
        username_data = json.load(usernamefile)
    data = {
        'indexfolders': indexerdata,
        'theme': themedata,
        'usernames': f"{username_data}"
    }
    json.dump(data, f)
    print('Successfully exported the data')
    f.close()


def import_data():
    try:
        from tkinter import filedialog
        from os import getcwd, remove
        initpth = getcwd() + "\\resources\\ initial.elsa"
        indexerpth = getcwd() + f"\\resources\\ indexerpaths.elsa"
        f = filedialog.askopenfile(mode='r', defaultextension=".json")
        data = json.load(f)
        indexdata = data.get('indexfolders')
        themedata = data.get('theme')
        usernamedata = data.get('usernames')
        print(indexdata, themedata)
        if indexdata is not None:
            indexfile = open(indexerpth, 'w')
            json.dump(indexdata, indexfile)
            indexfile.close()
            print('Imported the additional indexed folders')
            try:
                removepth = indexerpth = getcwd(
                ) + f"\\resources\\ indexer.elsa"
                remove(removepth)
                print("Deleted 'indexer.elsa'")
            except:
                pass
        themefile = open(initpth, 'w')
        themefile.write(f"{themedata[0]};{themedata[1]};{themedata[2]}")
        themefile.close()
        print('Imported the themes')
        USERNAMEPATH = getcwd() + f"\\resources\\ users.elsa"
        userfile = open(USERNAMEPATH, 'w')
        # see https://stackoverflow.com/questions/39491420/python-jsonexpecting-property-name-enclosed-in-double-quotes
        #json doesn't allow single qoutes. Only allows double qoutes
        usernamedata = usernamedata.replace("\'", '\"')
        usernamedata = json.loads(usernamedata)

        json.dump(usernamedata, userfile)
        print('Imported usernames')
        f.close()
    except Exception as e:
        print('Some error happened', e)
