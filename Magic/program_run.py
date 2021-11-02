from difflib import get_close_matches

from task1 import task

programdict = {"firefox": task.firefox, "ff": task.firefox, "photoshop": task.photoshop, "ps": task.photoshop,
               "word": task.msword, "msword": task.msword, "doc": task.msword, "powerpoint": task.powerpoint,
               "ppt": task.powerpoint, "vsc": task.vscode, "vscode": task.vscode, "wa": task.whatsapp,
               "msg": task.whatsapp, "whatsapp": task.whatsapp, "wordpad": task.wordpad, "wp": task.wordpad,
               "gimp": task.gimp, "vlc": task.vlc, "telegram": task.telegram, "tg": task.telegram,
               "notepad": task.notepad, "note": task.notepad, "calc": task.calc, "calculator": task.calc}
programlist = [i for i in programdict]


def program_run(afterkeyword: str) -> None:
    try:
        print("Approximate to", approx_program := get_close_matches(afterkeyword, programlist, n=1, cutoff=0.7))
        programdict[approx_program[0]]()
    except: print("Sorry the program is not yet supported.Please request the developer for more info.")
