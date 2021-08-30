import json
from Magic import theme, indexer


def export():
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
    data = {'indexfolders': indexerdata, 'theme': themedata}
    json.dump(data, f)
    f.close()
    print('Successfully exported the data')


def import_data():
    try:
        from tkinter import filedialog
        import os
        initpth = os.getcwd() + "\\resources\\ initial.elsa"
        indexerpth = os.getcwd() + f"\\resources\\ indexerpaths.elsa"
        f = filedialog.askopenfile(mode='r', defaultextension=".json")
        data = json.load(f)
        indexdata = data.get('indexfolders')
        themedata = data.get('theme')
        print(indexdata, themedata)
        if indexdata is not None:
            indexfile = open(indexerpth, 'w')
            json.dump(indexdata, indexfile)
            indexfile.close()
            print('Imported the additional indexed folders')
            try:
                removepth = indexerpth = os.getcwd() + f"\\resources\\ indexer.elsa"
                os.remove(removepth)
                print("Deleted 'indexer.elsa'")
            except:
                pass
        themefile = open(initpth, 'w')
        themefile.write(f"{themedata[0]};{themedata[1]};{themedata[2]}")
        themefile.close()
        print('Imported the themes')
        f.close()
    except Exception as e:
        print('Some error happened', e)
