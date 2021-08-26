from functools import partial
from tkinter import *

import Magic.about_page as about_page
import Magic.add_user as add_user
import Magic.history as history
import Magic.theme as theme
import Magic.tkinterlib as tkinterlib
from talk1.talk1 import talk


def setting_page(event="", username='', state=True):
    """[GUI for the settings page]

    Args:
        event (str, optional): [Not important]. Defaults to "".
        username (str, optional): [Username of the user using the GUI]. Defaults to ''.
        state (bool, optional): [Not important]. Defaults to True.
    """
    settingspage = Tk()
    bg_colour, text_color, button_colour = theme.read_theme()
    tkinterlib.tkinter_initialise(settingspage, 400, 340, top=0)
    a = LabelFrame(settingspage, text="Settings", bg=bg_colour, fg=text_color)
    a.pack()

    def usr_page(event=''):
        talk('Please add a new user')
        add_user.user_page()

    def abt_page():
        talk('Here is the about page')
        about_page.about_page()

    # Learn abt partial methods here: https://www.geeksforgeeks.org/partial-functions-python/

    adduser = Button(a,
                     text="Add User",
                     bd=0,
                     command=usr_page,
                     bg=bg_colour,
                     fg=text_color)
    adduser.pack(fill='x')
    # hover effect
    adduser.bind('<Enter>', partial(tkinterlib.on_enter, but=adduser))
    adduser.bind('<Leave>', partial(tkinterlib.on_leave, but=adduser))
    about = Button(a,
                   text="About",
                   command=abt_page,
                   bd=0,
                   bg=bg_colour,
                   fg=text_color)
    about.pack(fill='x')
    # hover effect
    about.bind('<Enter>', partial(tkinterlib.on_enter, but=about))
    about.bind('<Leave>', partial(tkinterlib.on_leave, but=about))

    change_theme = Button(a,
                          text="Change Theme",
                          command=theme.theme_selector,
                          bd=0,
                          bg=bg_colour,
                          fg=text_color)
    change_theme.pack(fill='x')
    # Hover effect
    change_theme.bind('<Enter>', partial(tkinterlib.on_enter,
                                         but=change_theme))
    change_theme.bind('<Leave>', partial(tkinterlib.on_leave,
                                         but=change_theme))

    if state:
        # Show history button
        showhis = Button(a,
                         text="Show History",
                         bd=0,
                         bg=bg_colour,
                         fg=text_color,
                         command=partial(history.user_read, username=username))

        showhis.pack(fill='x')
        # hover effect
        showhis.bind('<Enter>', partial(tkinterlib.on_enter, but=showhis))
        showhis.bind('<Leave>', partial(tkinterlib.on_leave, but=showhis))
        # clear history button
        clearhis = Button(a,
                          text="Clear History",
                          bd=0,
                          bg=bg_colour,
                          fg=text_color,
                          command=lambda: history.clear_history(username))
        clearhis.pack(fill='x')
        # hover effect
        clearhis.bind('<Enter>', partial(tkinterlib.on_enter, but=clearhis))
        clearhis.bind('<Leave>', partial(tkinterlib.on_leave, but=clearhis))
    # Close button
    close = Button(settingspage,
                   text="x",
                   font='bold',
                   bd=0,
                   bg=bg_colour,
                   fg=text_color,
                   command=settingspage.destroy)
    close.pack()
    # hover effect
    close.bind('<Enter>', partial(tkinterlib.on_enter, but=close))
    close.bind('<Leave>', partial(tkinterlib.on_leave, but=close))
    settingspage.mainloop()
