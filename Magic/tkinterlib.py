"""This  module is for stylising the Tkinter GUI"""
from functools import partial
from tkinter import Button, Label, LabelFrame

from Magic import theme

bg_colour, text_color, button_colour = theme.read_theme()


def tkinter_initialise(a, x: int = 0, y: int = 0, top: int = 1, noborders: bool = True, opacity: float = 0.9) -> None:
    """Used to mordernify tkinter gui boxes"""
    a.withdraw()  # Hide tkinter windows to finish initialization
    a.attributes("-alpha", opacity)  # Opacity of tkinter window
    a.overrideredirect(noborders)  # Remove Borders and default title bars
    a.configure(bg=bg_colour)
    a.attributes("-topmost", top)  # Decides if the tkinter windows shld always be on the top of other window
    a.geometry(f"+{x}+{y}")  # positions tkinter windows at x and y coordinate
    a.deiconify()  # show the tkinter window back


def on_enter(event, but: object) -> None:
    """[Part of hover effect for buttons]"""
    but.config(bg=button_colour)
    but.config(fg=bg_colour)


def on_leave(event, but: object) -> None:
    """[Part of hover effect for buttons]"""
    but.config(bg=bg_colour)
    but.config(fg=text_color)


def reset_colors() -> None:
    "Force reset the colours when user changes theme"
    global bg_colour, text_color, button_colour
    bg_colour, text_color, button_colour = theme.read_theme()


def TButton(root: object, text: str = "", command: object = None, relief: str = "ridge") -> object:
    "Customised Tkinter button"
    b = Button(root, text=text, fg=text_color, bd=0, bg=bg_colour, command=command, relief=relief)
    b.bind("<Enter>", partial(on_enter, but=b))
    b.bind("<Leave>", partial(on_leave, but=b))
    return b


def TLabel(root: object, text: str = "") -> object:
    "Customised tkinter Label"
    return Label(root, text=text, fg=text_color, bg=bg_colour)


def TLabelFrame(root: object, text: str = "") -> object:
    "Customised tkinter LabelFrame"
    return LabelFrame(root, text=text, fg=text_color, bg=bg_colour)
