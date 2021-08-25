'''Created by George Rahul
GUI for the login page'''

from tkinter import *

import Magic.theme as theme
import Magic.tkinterlib as tkinterlib
from functools import partial
from Magic.add_user import user_page


def SecurityUI():
    """[Login page]

    Returns:
        [str,str]: [Returns the password and username entered in the login page]
    """
    bg_colour, text_color, button_colour = theme.read_theme()
    #.................initialising tkinter........................
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
    #........entry fileds for username and password.............
    e = Entry(win, show="*", fg=text_color, width=10)
    e.place(x=104, y=30)
    e1 = Entry(win, width=10, fg=text_color)
    e1.place(x=104, y=10)

    #..........Labels for username and password............................................
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

    win1 = Toplevel(t)
    win1.withdraw()
    win1.lift()

    #win1.attributes("-topmost", 1)

    def password(event=''):
        """[Used to get the username and passowrd enerted]

        Args:
            event (str, optional): [Not important]. Defaults to ''.
        """
        password.passgui = e.get()
        password.usergui = e1.get()

        t.destroy()

    setins = Button(win,
                    text="Add User",
                    bd=0,
                    bg=bg_colour,
                    fg=text_color,
                    command=user_page)
    close_button = Button(win,
                          text="x",
                          font="bold",
                          bd=0,
                          bg=bg_colour,
                          fg=text_color,
                          command=exit)
    close_button.place(x=30, y=60)
    close_button.bind('<Enter>', partial(tkinterlib.on_enter,
                                         but=close_button))
    close_button.bind('<Leave>', partial(tkinterlib.on_leave,
                                         but=close_button))

    setins.place(x=120, y=60)
    setins.bind('<Enter>', partial(tkinterlib.on_enter, but=setins))
    setins.bind('<Leave>', partial(tkinterlib.on_leave, but=setins))

    ver = Button(win,
                 text='Verify',
                 bd=0,
                 command=password,
                 bg=bg_colour,
                 fg=text_color)
    ver.place(x=70, y=60)
    ver.bind('<Enter>', partial(tkinterlib.on_enter, but=ver))
    ver.bind('<Leave>', partial(tkinterlib.on_leave, but=ver))
    win.bind("<Return>", password)
    t.mainloop()
    return password.usergui, password.passgui
