"""This module is for syntax highlighting"""
from tkinter import END

from Magic import theme

keywords = [
    "search", "browse", "srch", "s",
    "msg",
    "bye", "tata", "close", "exit",
    "open", "o", "folder",
    "file", "f",
    "run",
    "firefox",
    "settings", "setting",
    "time",
    "website", "w",
    "ver", "what",
    "hello", "hlo", "hey",
    "hi",
    "download",
    "desktop",
    "music",
    "sh", "show",
    "clear",
    "joke", "tell",
    "shutdown",
    "restart",
    "open"]


def syntax_highlighting(event="", Search_box=None) -> None:
    """Function for syntax highlighting"""
    try:
        ord = Search_box.get()
        text_color = theme.read_theme()[1]
        if ord.split()[0].lower() in keywords:
            Search_box.delete(0, END)
            Search_box.config(fg="light green")
        else:
            Search_box.delete(0, END)
            Search_box.config(fg=text_color)
        Search_box.insert(0, ord)
        del Search_box, ord, text_color
    except: pass
