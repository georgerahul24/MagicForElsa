import gc
import json
import os, webbrowser
from talk1 import talk1
from difflib import get_close_matches
from pathlib import Path
from threading import Thread

indexerpth = os.getcwd() + f"\\resources\\ indexer.elsa"
# get path of the current file os.getcwd
# convert it into path use path(os.getcwd) use is_file() to check if it is a file
desktop = Path(os.path.join(os.path.join(os.environ["USERPROFILE"]),
                            "Desktop"))
documents = Path(
    os.path.join(os.path.join(os.environ["USERPROFILE"]), "Documents"))
downloads = Path(
    os.path.join(os.path.join(os.environ["USERPROFILE"]), "Downloads"))
music = Path(os.path.join(os.path.join(os.environ["USERPROFILE"]), "Music"))
videos = Path(os.path.join(os.path.join(os.environ["USERPROFILE"]), "Videos"))
directories = [desktop, documents, downloads, music, videos]


def indexer_folders():
    try:
        import json

        folderpth = indexerpth = os.getcwd(
        ) + f"\\resources\\ indexerpaths.elsa"
        with open(folderpth) as f:
            folders = json.load(f)
        return folders
    except:
        pass


def index(dataOfDirectories, pathn):
    """[Used to index files]

    Args:
        pathn ([str]): [Path of the parent folder to index]
    """

    try:

        for name in os.listdir(pathn):
            ine = os.path.join(pathn, name)
            i = Path(ine)
            if i.is_file():
                name = name.split(".")[0]
                print(f"filename:{name},path={ine}")
                dataOfDirectories[name.lower()] = ine

            elif name.startswith(".") == False and name.startswith(
                    "__") == False:
                try:
                    index(dataOfDirectories, i)
                except Exception as e:
                    print(e)

    except Exception as e:
        print(e)


def index_files():
    """[Check if the indexer.elsa file exists.If it exists,no action is taken.If it doesnt exists,files are indexed]"""
    cache_file = Path(indexerpth)
    def _index_files():
        if cache_file.exists() != True:
            with open(indexerpth, "w") as cache:
                print("'indexer.elsa' not found")
                print("Indexing files...Wait a moment...")
                folders = indexer_folders()
                try:
                    directories.extend(folders)
                except:
                    pass
                dataOfDirectories = {}
                for paths in directories:
                    index(dataOfDirectories, paths)
                print(dataOfDirectories)
                json.dump(dataOfDirectories, cache)
                print("Json dumped")
        else:
            print("'indexer.elsa' found")
    Thread(target=_index_files).start()

def search_indexed_file(filename):
    import json

    with open(indexerpth, "r") as cache:
        cachedict = json.load(cache)
    filenames = [data for data in cachedict]

    approx_file = get_close_matches(filename, filenames, n=1, cutoff=0.7)

    try:
        print("Approximate to", approx_file[0])
        if len(approx_file) != 0 and len(approx_file[0]) != 0:

            srched_filepath = cachedict[approx_file[0]]

            webbrowser.open(srched_filepath)

            print(f"Opened {srched_filepath}")
            talk1.talk(f"Opened {approx_file}")
        else:
            print(f"Could not find any files")
            talk1.talk(f"Could not find any files")
        del cachedict,filenames,approx_file,cache,srched_filepath
        gc.collect()
    except:
        print(f"Could not find any files")
        talk1.talk(f"Could not find any files")


def add_indexer_folders(event="", path=""):
    try:
        import json

        folderpth = os.getcwd() + f"\\resources\\ indexerpaths.elsa"
        with open(folderpth) as f:
            folders = json.load(f)
            folders.append(path)
        with open(folderpth, "w") as f:
            json.dump(folders, f)

    except:
        import json
        folderpth = os.getcwd(
        ) + f"\\resources\\ indexerpaths.elsa"
        with open(folderpth, "w") as f:
            json.dump([path], f)
    try:
        removepth = os.getcwd() + f"\\resources\\ indexer.elsa"
        os.remove(removepth)
    except:
        pass
    del folderpth,folders,f
    gc.collect()

def read_indexer_folders(event=""):
    try:
        import json

        folderpth  = os.getcwd(
        ) + f"\\resources\\ indexerpaths.elsa"
        with open(folderpth) as f:
            folders = json.load(f)
        return folders
    except:
        pass


# run index files when indexer module is imported in Elsa
index_files()
