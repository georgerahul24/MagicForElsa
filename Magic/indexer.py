import json
import os
import pickle
import webbrowser
from difflib import get_close_matches
from pathlib import Path
from threading import Thread

from talk1 import talk1

indexerpth, indexerfolderpth = (os.getcwd() + "\\resources\\ indexer.elsa"), (os.getcwd() + "\\resources\\ indexerfolder.elsa")
directories = [desktop := Path(os.path.join(os.path.join(os.environ["USERPROFILE"]), "Desktop")),
               documents := Path(os.path.join(os.path.join(os.environ["USERPROFILE"]), "Documents")),
               downloads := Path(os.path.join(os.path.join(os.environ["USERPROFILE"]), "Downloads")),
               music := Path(os.path.join(os.path.join(os.environ["USERPROFILE"]), "Music")),
               videos := Path(os.path.join(os.path.join(os.environ["USERPROFILE"]), "Videos"))]
cacheData = dict()


def read_indexer_folders(event="") -> list:
    """To get the list of folders that should be indexed additionally"""
    try:
        with open((os.getcwd() + "\\resources\\ indexerpaths.elsa")) as f:
            return json.load(f)
    except: pass


def cachesearch(func):
    """To search for file/folder in the cache"""

    def _cachesearch(args: tuple):
        try:
            webbrowser.open(cacheData[args])
            print("Opened from cache")
            talk1.talk(f"opened {args}")
        except:
            if (filepath := func(args)) is not None: cacheData[args] = filepath

    return _cachesearch


def index(dataOfDirectories: dict, dataofFolders: dict, pathn: str) -> None:
    """[Used to index files]"""
    try:
        for name in os.listdir(pathn):
            i = Path((ine := os.path.join(pathn, name)))
            if i.is_file():
                name = name.split(".")[0]
                dataOfDirectories[name.lower()] = ine
            elif name.startswith(".") == False and name.startswith("__") == False:
                try:
                    dataofFolders[name.lower()] = ine
                    index(dataOfDirectories, dataofFolders, i)
                except Exception as e: print(e)
    except Exception as e: print(e)


def index_files() -> None:
    """[Check if the indexer.elsa file exists.If it exists,no action is taken.If it doesnt exists,files are indexed]"""

    def _index_files():
        if Path(indexerpth).exists() != True:
            print("'indexer.elsa' not found", "\nIndexing files...Wait a moment...")
            try: directories.extend(read_indexer_folders())
            except: pass
            dataOfDirectories, dataOfFolders, proc = {}, {}, []
            for paths in directories:
                p = Thread(target=index, args=(dataOfDirectories, dataOfFolders, paths))
                proc.append(p)
                p.start()
            print("Indexing Threads:", *proc)
            for p in proc:
                p.join()
            with open(indexerpth, "wb") as cache:
                pickle.dump(dataOfDirectories, cache)
            with open(indexerfolderpth, "wb") as cache2:
                pickle.dump(dataOfFolders, cache2)
            del cache, dataOfDirectories, dataOfFolders
            print("All indexing processes functions finished,files updated")
            global cacheData
            cacheData = {}  # Resetting cache dict to avoid errors and such
        else: print("'indexer.elsa' found")

    Thread(target=_index_files).start()


@cachesearch
def search_indexed_file(filename: str) -> None:
    """Search and open  a file that is indexed"""
    with open(indexerpth, "rb") as cache:
        cache_dict = pickle.load(cache)
    print("Approximate to", approx_file := get_close_matches(filename, filenames := [data for data in cache_dict], n=1, cutoff=0.7))
    try:
        if len(approx_file) != 0 and len(approx_file[0]) != 0:
            webbrowser.open(srched_filepath := cache_dict[approx_file[0]])
            print(f"Opened {srched_filepath}")
            talk1.talk(f"Opened {approx_file}")
            del cache_dict, filenames, approx_file, cache
            return srched_filepath
        else:
            print(f"Could not find any files")
            talk1.talk("Could not find any files")
    except:
        print("Could not find any files")
        talk1.talk(f"Could not find any files")


@cachesearch
def search_indexed_folder(filename: str) -> None:
    """Search and open a folder that has been indexed"""
    try:
        with open(indexerfolderpth, "rb") as cache:
            cache_dict = pickle.load(cache)
        print("Approximate to", approx_folder := get_close_matches(filename, folder_names := [data for data in cache_dict], n=1, cutoff=0.7))
        try:
            if len(approx_folder) != 0 and len(approx_folder[0]) != 0:
                webbrowser.open(srched_folderpath := cache_dict[approx_folder[0]])
                print(f"Opened {srched_folderpath}")
                talk1.talk(f"Opened {approx_folder}")
                del cache_dict, approx_folder, cache, folder_names
                return srched_folderpath
            else:
                print(f"Could not find any folders")
                talk1.talk("Could not find any folders")
        except:
            print("Could not find any folders")
            talk1.talk(f"Could not find any folders")
    except: print("There is a problem with indexed file data.PLease reset the indexer data")


def add_indexer_folders(event="", path: str = "") -> None:
    """Add additional folders that should be indexed"""
    folderpth = os.getcwd() + f"\\resources\\ indexerpaths.elsa"
    try:
        with open(folderpth) as f:
            folders = json.load(f)
            # ...Converting to set to avoid duplicates.....
            # ...Keeping it as list itself because other files expect this to be a list due to legacy reasons,etc,etc
            folders = list(set(folders.append(path)))  # ADDING PATH TO THE FOLDERS LIST
        with open(folderpth, "w") as f:
            json.dump(folders, f, indent=4)
        del folderpth, folders, f
    except:
        with open(folderpth, "w") as f:
            json.dump([path], f, indent=4)
    try: os.remove((os.getcwd() + "\\resources\\ indexer.elsa"))
    except: pass
