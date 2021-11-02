import os
from tkinter.colorchooser import askcolor


def read_theme() -> tuple:
    """Reads the theme from the initial.elsa file"""
    try:
        with open((os.getcwd() + "\\resources\\ initial.elsa")) as f:
            datas = f.read()
        colours = datas.split(";")
        bg_colour, text_color, button_colour = colours[0].rstrip().lstrip(), colours[1].rstrip().lstrip(), \
                                               colours[2].split("\n")[0].rstrip().lstrip()
        return bg_colour, text_color, button_colour
    except Exception as e:print("initial.elsa is corrupted", e)


def theme_writer(bg_colour: str, font_colour: str, button_colour: str) -> None:
    """To wrote the new theme"""
    initpth = os.getcwd() + "\\resources\\ initial.elsa"
    with open(initpth, "w") as f:
        f.write(f"{bg_colour};{font_colour};{button_colour}\n#The order is bg,font color,button colour\n#Please remember to use ';' to separate colours")
    del bg_colour, font_colour, button_colour


def new_background_colour(event="") -> None:
    """To add the new background colour"""
    bg_colour, text_color, button_colour = read_theme()
    if (color := askcolor()[1]) is not None:
        theme_writer(color, text_color, button_colour)


def new_font_colour(event="") -> None:
    """To add the new font colour"""
    bg_colour, text_color, button_colour = read_theme()
    if (color := askcolor()[1]) is not None:
        theme_writer(bg_colour, color, button_colour)


def new_button_colour(event="") -> None:
    """To add the new button colour"""
    bg_colour, text_color, button_colour = read_theme()
    if (color := askcolor()[1]) is not None:
        theme_writer(bg_colour, text_color, color)
