from tkinter import Tk, Label, LabelFrame, Button, Entry
from Magic import tkinterlib, file_database, theme
from talk1.talk1 import talk

from functools import partial


def user_page():
    """[This function is used to implement the GUI of the add user page]
    """
    userpage = Tk()

    bg_colour, text_color, button_colour = theme.read_theme()
    tkinterlib.tkinter_initialise(userpage, 600, 340)
    s = LabelFrame(userpage, text="Add New User", bg=bg_colour, fg=text_color)
    s.grid(row=0, column=0)

    lu = Label(s, text="Enter the username:", bg=bg_colour, fg=text_color)
    lp = Label(s, text="Enter the password:", bg=bg_colour, fg=text_color)
    eu = Entry(s)
    ep = Entry(s)

    def add_user_layout():
        """[Placing the elemnts in the settings page]
        """
        lu.grid(row=0, column=0)
        eu.grid(row=0, column=1)
        lp.grid(row=1, column=0)
        ep.grid(row=1, column=1)

    def add(event=''):
        """[Adds the user]

        Args:
            event (str, optional): [Not important]. Defaults to ''.
        """

        new_user = eu.get()
        new_password = ep.get()
        state = file_database.write_to_file(new_user, new_password)
        if state == 1:
            talk(f'Successfully added {new_user}')

        elif state == -1:
            talk("user aldready exists. Try again")
        userpage.destroy()

    add_user_layout()
    add_user_button = Button(s,
                             text="Add User",
                             bd=0,
                             command=add,
                             bg=bg_colour,
                             fg=text_color)
    add_user_button.grid(row=3, column=1)
    add_user_button.bind('<Enter>',
                         partial(tkinterlib.on_enter, but=add_user_button))
    add_user_button.bind('<Leave>',
                         partial(tkinterlib.on_leave, but=add_user_button))
    close_button = Button(s,
                          text="X",
                          font="Bold",
                          bg=bg_colour,
                          fg=text_color,
                          command=userpage.destroy,
                          bd=0)

    close_button.grid(row=3, column=0)

    close_button.bind('<Enter>', partial(tkinterlib.on_enter,
                                         but=close_button))
    close_button.bind('<Leave>', partial(tkinterlib.on_leave,
                                         but=close_button))
    userpage.bind("<Return>", add)
    userpage.mainloop()
