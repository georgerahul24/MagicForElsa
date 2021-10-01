"""Created by George Rahul
GUI for the login page"""

from tkinter import Tk, Toplevel, Entry, Label

from Magic import theme
from Magic.usergui import user_page
from Magic.tkinterlib import TButton


def SecurityUI():
    """[Login page]

    Returns:
        [str,str]: [Returns the password and username entered in the login page]
    """
    bg_colour, text_color, button_colour = theme.read_theme()
    # .................initialising tkinter........................
    t = Tk()
    t.withdraw()
    # t.deiconify() to make it appear again
    win = Toplevel(t)
    win.geometry("200x100+700+300")
    win.config(bg=bg_colour)
    win.overrideredirect(True)
    win.attributes("-topmost", 1)
    win.attributes("-alpha", 0.8)

    # win.overrideredirect(1)
    # ........entry fileds for username and password.............
    e = Entry(win, show="*", fg=text_color, width=10)
    e.place(x=104, y=30)
    e1 = Entry(win, width=10, fg=text_color)
    e1.place(x=104, y=10)

    # ..........Labels for username and password............................................
    t1 = Label(win,
               text="Username:",
               bg=bg_colour,
               fg=text_color,
               font="Nebula 10 bold").place(x=20, y=10)
    t2 = Label(win,
               text="Password:",
               bg=bg_colour,
               fg=text_color,
               font="Nebula 10 bold").place(x=20, y=30)

    def password(event=""):
        """[Used to get the username and passowrd enerted]

        Args:
            event (str, optional): [Not important]. Defaults to ''.
        """
        password.passgui = e.get()
        password.usergui = e1.get()

        t.destroy()

    setins = TButton(win, text="Add User", command=user_page)
    close_button = TButton(win, text="x", command=exit)
    close_button.place(x=30, y=60)

    setins.place(x=120, y=60)

    ver = TButton(
        win,
        text="Verify",
        command=password,
    )
    ver.place(x=70, y=60)

    win.bind("<Return>", password)
    t.mainloop()
    return password.usergui, password.passgui
