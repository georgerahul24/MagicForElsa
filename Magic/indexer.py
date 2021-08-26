import os, webbrowser
from talk1 import talk1
from difflib import get_close_matches
from pathlib import Path

indexerpth = os.getcwd() + f'\\resources\\ indexer.elsa'
# get path of the current file os.getcwd
# convert it into path use path(os.getcwd) use is_file() to check if it is a file
desktop = Path(os.path.join(os.path.join(os.environ['USERPROFILE']),
                            'Desktop'))
documents = Path(
    os.path.join(os.path.join(os.environ['USERPROFILE']), 'Documents'))
downloads = Path(
    os.path.join(os.path.join(os.environ['USERPROFILE']), 'Downloads'))
music = Path(os.path.join(os.path.join(os.environ['USERPROFILE']), 'Music'))
videos = Path(os.path.join(os.path.join(os.environ['USERPROFILE']), 'Videos'))
directories = [desktop, documents, downloads, music, videos]


def index(pathn):
    """[Used to index files]

    Args:
        pathn ([str]): [Path of the parent folder to index]
    """
    cache = open(indexerpth, 'a')
    try:

        for name in os.listdir(pathn):
            i = os.path.join(pathn, name)
            i = Path(i)
            if i.is_file() == True:
                name = name.split('.')[0]
                print(i, name, sep=" !@#$%^& ")

                cache.write(f"{name} @#$%^& {i} @#$%^& \n")

            else:  #check for the files in a directories by calling the function recursively
                if name.startswith('.') == False and name.startswith(
                        '__') == False:
                    try:
                        index(i)
                    except Exception as e:
                        print(e)
        cache.flush()
    except Exception as e:
        print(e)
    cache.close()


def index_files():
    """[Check if the indexer.elsa file exists.If it exists,no action is taken.If it doesnt exists,files are indexed]
    """
    cache_file = Path(indexerpth)

    if cache_file.exists() == True:
        print("'indexer.elsa' found")
    else:
        cache = open(indexerpth, 'w')
        cache.close()
        print("'indexer.elsa' not found")
        print("Indexing files...Wait a moment...")
        for paths in directories:
            index(paths)


def search_indexed_file(filename):
    """[Searches for the filename and opens it if it is found]

    Args:
        filename ([str]): [Name of the file to be opened]
    """
    try:

        cache = open(indexerpth, 'r')
        datas = cache.readlines()
        cache.close()
        cachedict = {}
        filenames = []
        for data in datas:
            data = data.split(' @#$%^& ')
            cachedict[data[0]] = data[1]
            filenames.append(data[0])
        approx_file = get_close_matches(filename, filenames, n=1, cutoff=0.7)
        print(approx_file)
        if len(approx_file) != 0:
            srched_filepath = cachedict[approx_file[0]]
            webbrowser.open(srched_filepath)
            print(f'Opened {srched_filepath}')
            talk1.talk(f'Opened {approx_file[0]}')
        else:
            print(f'Could not find any files')
            talk1.talk(f'Could not find any files')
    except Exception as e:
        print('Error:', e)


#run index files when indexer module is imported in Elsa
index_files()
