from Magic import theme
from tkinter import END


def syntax_highlighting(event="", Search_box=None) -> None:

    try:
        ord = Search_box.get()
        bg_colour, text_color, button_colour = theme.read_theme()
        keyword = ord.split()[0].lower()
        keywords = [
            "search",
            "browse",
            "srch",
            "msg",
            "whatsapp",
            "bye",
            "tata",
            "close",
            "exit",
            "file",
            "f",
            "run",
            "theme",
            "firefox",
            "settings",
            "setting",
            "time",
            "ver",
            "what",
            "hello",
            "hlo",
            "hey",
            "hi",
            "download",
            "desktop",
            "music",
            "sh",
            "show",
            "clear",
            "joke",
            "shutdown",
            "restart",
            "open",
        ]
        if keyword in keywords:
            Search_box.delete(0, END)
            Search_box.config(fg="light green")
        else:
            Search_box.delete(0, END)
            Search_box.config(fg=text_color)
        Search_box.insert(0, ord)

    except:
        pass
