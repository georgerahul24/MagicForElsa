import gc
import os
import pickle
import webbrowser
from difflib import get_close_matches
from pathlib import Path
from threading import Thread

from talk1 import talk1

indexerpth = os.getcwd() + f"\\resources\\ indexer.elsa"
indexerfolderpth = os.getcwd() + f"\\resources\\ indexerfolder.elsa"
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
cacheinfo = dict()


def cachesearch(func):
    def _cachesearch(args):

        try:
            filepth = cacheinfo[args]

            print("Opening from cache")
            webbrowser.open(filepth)

            talk1.talk(f"opened {args}")

        except:
            filepath = func(args)

            if filepath is not None:
                cacheinfo[args] = filepath

    return _cachesearch


def indexer_folders():
    try:
        import json
        folderpth = (os.getcwd() + '\\resources\\ indexerpaths.elsa')
        with open(folderpth) as f:
            folders = json.load(f)
        return folders
    except:
        pass


def index(dataOfDirectories, dataofFolders, pathn):
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

                dataOfDirectories[name.lower()] = ine

            elif name.startswith(".") == False and name.startswith(
                    "__") == False:
                try:
                    dataofFolders[name.lower()] = ine
                    index(dataOfDirectories, dataofFolders, i)
                except Exception as e:
                    print(e)

    except Exception as e:
        print(e)


def index_files():
    """[Check if the indexer.elsa file exists.If it exists,no action is taken.If it doesnt exists,files are indexed]"""
    cache_file = Path(indexerpth)
    folder_file = Path(indexerfolderpth)

    def _index_files():
        if cache_file.exists() != True:

            print("'indexer.elsa' not found")
            print("Indexing files...Wait a moment...")
            folders = indexer_folders()
            try:
                directories.extend(folders)
            except:
                pass
            dataOfDirectories = {}
            dataOfFolders = {}
            proc = []
            for paths in directories:
                p = Thread(target=index,
                           args=(dataOfDirectories, dataOfFolders, paths))
                proc.append(p)
                p.start()

            print("Indexing Threads:", *proc)
            for p in proc:
                p.join()
                print(p, "finished")
            print("All indexing processes functions finished")
            with open(indexerpth, "wb") as cache:
                pickle.dump(dataOfDirectories, cache)
            with open(indexerfolderpth, 'wb') as cache2:
                pickle.dump(dataOfFolders, cache2)
            del cache, dataOfDirectories, dataOfFolders
            gc.collect()
            print("Json dumped and cleaned")
        else:
            print("'indexer.elsa' found")

    Thread(target=_index_files).start()


@cachesearch
def search_indexed_file(filename):
    with open(indexerpth, "rb") as cache:
        cachedict = pickle.load(cache)
    filenames = [data for data in cachedict]

    approx_file = get_close_matches(filename, filenames, n=1, cutoff=0.7)

    try:
        print("Approximate to", approx_file[0])
        if len(approx_file) != 0 and len(approx_file[0]) != 0:

            srched_filepath = cachedict[approx_file[0]]

            webbrowser.open(srched_filepath)

            print(f"Opened {srched_filepath}")
            talk1.talk(f"Opened {approx_file}")
            del cachedict, filenames, approx_file, cache
            gc.collect()
            return srched_filepath

        else:
            print(f"Could not find any files")
            talk1.talk('Could not find any files')

    except:
        print('Could not find any files')
        talk1.talk(f"Could not find any files")


@cachesearch
def search_indexed_folder(filename):
    try:
        with open(indexerfolderpth, "rb") as cache:
            cachedict = pickle.load(cache)
        filenames = [data for data in cachedict]

        approx_file = get_close_matches(filename, filenames, n=1, cutoff=0.7)

        try:
            print("Approximate to", approx_file[0])
            if len(approx_file) != 0 and len(approx_file[0]) != 0:

                srched_filepath = cachedict[approx_file[0]]

                webbrowser.open(srched_filepath)

                print(f"Opened {srched_filepath}")
                talk1.talk(f"Opened {approx_file}")
                del cachedict, approx_file, cache, filenames
                gc.collect()
                return srched_filepath
            else:
                print(f"Could not find any folders")
                talk1.talk('Could not find any folders')

        except:
            print('Could not find any folders')
            talk1.talk(f"Could not find any folders")
    except:
        print(
            "There is a problem with indexed file data.PLease reset the indexer data"
        )


def add_indexer_folders(event="", path=""):
    try:
        import json

        folderpth = os.getcwd() + f"\\resources\\ indexerpaths.elsa"
        with open(folderpth) as f:
            folders = json.load(f)
            folders.append(path)
        with open(folderpth, "w") as f:
            json.dump(folders, f, indent=4)
        del folderpth, folders, f
    except:
        import json

        folderpth = os.getcwd() + '\\resources\\ indexerpaths.elsa'
        with open(folderpth, "w") as f:
            json.dump([path], f, indent=4)
    try:
        removepth = os.getcwd() + '\\resources\\ indexer.elsa'
        os.remove(removepth)
    except:
        pass

    gc.collect()


def read_indexer_folders(event=""):
    try:
        import json

        folderpth = os.getcwd() + '\\resources\\ indexerpaths.elsa'
        with open(folderpth) as f:
            folders = json.load(f)
        return folders
    except:
        pass


# run index files when indexer module is imported in Elsa
index_files()
