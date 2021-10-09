from task1 import task


def program_run(afterkeyword:str):
    if afterkeyword in ["firefox", "ff"]:
        task.firefox()
    elif afterkeyword in ["photoshop", "ps"]:
        task.photoshop()
    elif afterkeyword in ["word", "msword", "doc"]:
        task.msword()
    elif afterkeyword in ["powerpoint", "ppt"]:
        task.powerpoint()
    elif afterkeyword in ["vsc", "vscode"]:
        task.vscode()
    elif afterkeyword in ["wa", "msg", "whatsapp"]:
        task.whatsapp()
    elif afterkeyword in ["wordpad", "wp"]:
        task.wordpad()
    elif afterkeyword in [
            "gimp",
    ]:
        task.gimp()
    elif afterkeyword in [
            "vlc",
    ]:
        task.vlc()
    elif afterkeyword in ["telegram", "tg"]:
        task.telegram()
