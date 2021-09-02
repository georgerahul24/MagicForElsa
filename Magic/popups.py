import time
from tkinter import Tk, Button,Label
from task1.task import web
from Magic import tkinterlib, theme
from sys import exit


def popups(srch):
    """[A yes or no gui box to know if the user needs to search things in the internet]

    Args:
        srch ([str]): [The term to be searched in internet]
    """
    popups = Tk()
    bg_colour, text_color, button_colour = theme.read_theme()
    screen_height = popups.winfo_screenheight()
    screen_width = popups.winfo_screenwidth()
    tkinterlib.tkinter_initialise(popups,
                                  x=screen_width - 130,
                                  y=screen_height - 130)

    def srchYes(event=""):
        popups.destroy()
        web(srch)

    Yes = Button(popups,
                 text="Yes",
                 bg=button_colour,
                 fg=text_color,
                 command=srchYes)

    # function refernced in elsa.py
    def destroyPop():
        popups.destroy()

    No = Button(popups,
                text="No",
                bg=button_colour,
                fg=text_color,
                command=popups.destroy)
    Yes.grid(row=1, column=0)
    No.grid(row=1, column=1)
    popups.mainloop()

def resetelsapopup():
    import os
    import shutil
    from talk1.talk1 import talk
    from pathlib import Path
    popups = Tk()
    bg_colour, text_color, button_colour = theme.read_theme()
    screen_height, screen_width = popups.winfo_screenheight(), popups.winfo_screenwidth()

    tkinterlib.tkinter_initialise(popups,
                                  x=int(screen_width/2),
                                  y=int(screen_height/2))
    popups.geometry(f"193x50+{int(screen_width/2)}+{int(screen_height/2)}")
    talk("Are you sure that you want to reset Elsa")
    Label(popups,text="Are you sure you want to reset Elsa?",fg=text_color,bg=bg_colour).place(x=0,y=0)
    def Yes(event=""):
        talk("Please wait for a moment. Elsa is being reset")
        talk("Just run elsa after it shutdowns")
        print("Resetting Elsa")
        time.sleep(1)
        shutil.rmtree(Path(os.getcwd()+"\\resources"))
        exit()



    Yes = Button(popups,
                 text="Yes",
                 bg=button_colour,
                 fg=text_color,
                 command=Yes)

    # function refernced in elsa.py
    def destroyPop():
        popups.destroy()

    No = Button(popups,
                text="No",
                bg=button_colour,
                fg=text_color,
                command=popups.destroy)
    Yes.place(x=60,y=20)
    No.place(x=100,y=20)
    popups.mainloop()


if __name__ == "__main__":
    popups("George is the greatest person on the earth")
