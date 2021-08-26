from tkinter import Tk,Button
from task1.task import web
from Magic import tkinterlib,theme



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

    def srchYes(event=''):
        popups.destroy()
        web(srch)

    Yes = Button(popups,
                 text='Yes',
                 bg=button_colour,
                 fg=text_color,
                 command=srchYes)

    #function also  refernced in elsa.py
    def destroyPop():
        popups.destroy()

    No = Button(popups,
                text='No',
                bg=button_colour,
                fg=text_color,
                command=popups.destroy)
    Yes.grid(row=1, column=0)
    No.grid(row=1, column=1)
    popups.mainloop()


if __name__ == "__main__":
    popups('George is the greatest person on the earth')
