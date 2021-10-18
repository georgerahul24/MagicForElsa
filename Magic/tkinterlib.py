"""This  module is for stylising the Tkinter GUI"""
from functools import partial
from tkinter import Button

from Magic import theme

bg_colour, text_color, button_colour = theme.read_theme()


def tkinter_initialise(a, x: int = 0, y: int = 0, top: int = 1, noborders: bool = True, opacity: int = 0.9) -> None:
    """Used to mordernify tkinter gui boxes"""
    a.withdraw()  # Hide tkinter windows to finish initialization
    a.attributes("-alpha", opacity)  # Opacity of tkinter window
    a.overrideredirect(noborders)  # Remove Borders and default title bars
    a.configure(bg=bg_colour)
    a.attributes(
        "-topmost", top
    )  # Decides if the tkinter windows shld always be on the top of other window
    a.geometry(f"+{x}+{y}")  # positions tkinter windows at x and y coordinate

    a.deiconify()  # show the tkinter window back


def on_enter(event, but: object) -> None:
    """[Part of hover effect for buttons]"""
    # Change the button colour from background colour to button colour for
    # hover effect when mouse enters the button field
    but.config(bg=button_colour)
    but.config(fg=bg_colour)


def on_leave(event, but:object)->None:
    """[Part of hover effect for buttons]"""
    # Change back the button colour to background colour when mouse leaves the button field.
    but.config(bg=bg_colour)
    but.config(fg=text_color)

def TButton(root:object, text:str="", command:object=None, relief:str="ridge")->None:
    b = Button(root,text=text,fg=text_color,bd=0,bg=bg_colour,command=command,relief=relief)
    b.bind("<Enter>", partial(on_enter, but=b))
    b.bind("<Leave>", partial(on_leave, but=b))
    return b


def reset_colors()->None:
    global bg_colour, text_color, button_colour
    bg_colour, text_color, button_colour = theme.read_theme()
