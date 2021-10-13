"""
This module is for syntax highlighting
"""
import gc
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
    "open",
]


def syntax_highlighting(event="", Search_box=None) -> None:
    """Function for syntax highlighting"""
    try:
        ord = Search_box.get()
        bg_colour, text_color, button_colour = theme.read_theme()
        keyword = ord.split()[0].lower()
        if keyword in keywords:
            Search_box.delete(0, END)
            Search_box.config(fg="light green")
        else:
            Search_box.delete(0, END)
            Search_box.config(fg=text_color)
        Search_box.insert(0, ord)
        del Search_box, ord, bg_colour, text_color, button_colour, keyword
        gc.collect()
    except:
        pass
