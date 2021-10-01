"""
This module is to display GUI for adding and deleting users
"""

from functools import partial
from tkinter import Tk, Label, LabelFrame, Button, Entry

from talk1.talk1 import talk

from Magic import tkinterlib, file_database, theme


def user_page():
    """[This function is used to implement the GUI of the add user page]"""
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
        """[Placing the elements in the settings page]"""
        lu.grid(row=0, column=0)
        eu.grid(row=0, column=1)
        lp.grid(row=1, column=0)
        ep.grid(row=1, column=1)

    def add(event=""):
        """[Adds the user]

        Args:
            event (str, optional): [Not important]. Defaults to ''.
        """

        new_user = eu.get()
        new_password = ep.get()
        state = file_database.write_to_file(new_user, new_password)
        if state == 1:
            talk(f"Successfully added {new_user}")

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
    add_user_button.bind("<Enter>",
                         partial(tkinterlib.on_enter, but=add_user_button))
    add_user_button.bind("<Leave>",
                         partial(tkinterlib.on_leave, but=add_user_button))
    close_button = Button(
        s,
        text="X",
        font="Bold",
        bg=bg_colour,
        fg=text_color,
        command=userpage.destroy,
        bd=0,
    )

    close_button.grid(row=3, column=0)

    close_button.bind("<Enter>", partial(tkinterlib.on_enter,
                                         but=close_button))
    close_button.bind("<Leave>", partial(tkinterlib.on_leave,
                                         but=close_button))
    userpage.bind("<Return>", add)
    userpage.mainloop()


def user_page_init():
    """[This function is used to add a new user in the initial setup]"""
    userpage = Tk()
    data = []
    bg_colour, text_color, button_colour = theme.read_theme()
    tkinterlib.tkinter_initialise(userpage, 600, 340)
    s = LabelFrame(userpage, text="Add New User", bg=bg_colour, fg=text_color)
    s.grid(row=0, column=0)

    lu = Label(s, text="Enter the username:", bg=bg_colour, fg=text_color)
    lp = Label(s, text="Enter the password:", bg=bg_colour, fg=text_color)
    eu = Entry(s)
    ep = Entry(s)

    def add_user_layout():
        """[Placing the elemnts in the settings page]"""
        lu.grid(row=0, column=0)
        eu.grid(row=0, column=1)
        lp.grid(row=1, column=0)
        ep.grid(row=1, column=1)

    def add(event=""):
        """[Adds the user]

        Args:
            event (str, optional): [Not important]. Defaults to ''.
        """

        new_user = eu.get()
        new_password = ep.get()
        userpage.destroy()
        data.append(new_user)
        data.append(new_password)

    add_user_layout()
    add_user_button = Button(s,
                             text="Add User",
                             bd=0,
                             command=add,
                             bg=bg_colour,
                             fg=text_color)
    add_user_button.grid(row=3, column=1)
    add_user_button.bind("<Enter>",
                         partial(tkinterlib.on_enter, but=add_user_button))
    add_user_button.bind("<Leave>",
                         partial(tkinterlib.on_leave, but=add_user_button))
    close_button = Button(
        s,
        text="X",
        font="Bold",
        bg=bg_colour,
        fg=text_color,
        command=userpage.destroy,
        bd=0,
    )

    close_button.grid(row=3, column=0)

    close_button.bind("<Enter>", partial(tkinterlib.on_enter,
                                         but=close_button))
    close_button.bind("<Leave>", partial(tkinterlib.on_leave,
                                         but=close_button))
    userpage.bind("<Return>", add)
    userpage.mainloop()
    return data


def deleteuser():
    """[This function is used to implement the GUI of the add user page]"""
    deleteuserpage = Tk()
    talk("Please enter the username and password to delete")
    bg_colour, text_color, button_colour = theme.read_theme()
    tkinterlib.tkinter_initialise(deleteuserpage, 600, 340)
    s = LabelFrame(deleteuserpage,
                   text="Delete User",
                   bg=bg_colour,
                   fg=text_color)
    s.grid(row=0, column=0)

    lu = Label(s,
               text="Enter the username to delete:",
               bg=bg_colour,
               fg=text_color)
    lp = Label(s, text="Enter the password:", bg=bg_colour, fg=text_color)
    lpr = Label(s, text="Retype the password:", bg=bg_colour, fg=text_color)
    eu = Entry(s)
    ep = Entry(s)
    epr = Entry(s)

    def add_user_layout():
        """[Placing the elements in the settings page]"""
        lu.grid(row=0, column=0)
        eu.grid(row=0, column=1)
        lp.grid(row=1, column=0)
        ep.grid(row=1, column=1)
        lpr.grid(row=2, column=0)
        epr.grid(row=2, column=1)

    def deleteuserfunc(event=""):
        """[Adds the user]

        Args:
            event (str, optional): [Not important]. Defaults to ''.
        """

        name_delete = eu.get()
        password = ep.get()
        retypepassword = epr.get()
        if retypepassword == password:
            try:
                import json
                import os
                from pathlib import Path

                userpth = os.getcwd() + "\\resources\\ users.elsa"
                userfile = open(Path(userpth))
                userdata = json.load(userfile)
                userfile.close()

                try:
                    if userdata[name_delete] == password:
                        del userdata[name_delete]
                        deleteuserpage.destroy()
                        userfile = open(Path(userpth), "w")
                        if len(userdata) == 0:
                            userdata["admin"] = "1234"
                        json.dump(userdata, userfile, indent=4)
                        userfile.close()
                        talk("User successfully deleted")
                    else:
                        print("Sorry. your username and password do not match")
                        talk("Sorry. your username and password do not match")
                except:

                    talk("Sorry,such a user do not exist. Please try again")

            except:

                talk("Sorry, but the passwords do not match")
        else:
            print("Passwords in both the field do not match")
            talk("Passwords in both the field do not match. Please try again")

    add_user_layout()
    add_user_button = Button(s,
                             text="Delete User",
                             bd=0,
                             command=deleteuserfunc,
                             bg=bg_colour,
                             fg=text_color)
    add_user_button.grid(row=3, column=1)
    add_user_button.bind("<Enter>",
                         partial(tkinterlib.on_enter, but=add_user_button))
    add_user_button.bind("<Leave>",
                         partial(tkinterlib.on_leave, but=add_user_button))
    close_button = Button(
        s,
        text="X",
        font="Bold",
        bg=bg_colour,
        fg=text_color,
        command=deleteuserpage.destroy,
        bd=0,
    )

    close_button.grid(row=3, column=0)

    close_button.bind("<Enter>", partial(tkinterlib.on_enter,
                                         but=close_button))
    close_button.bind("<Leave>", partial(tkinterlib.on_leave,
                                         but=close_button))
    deleteuserpage.bind("<Return>", deleteuserfunc)
    deleteuserpage.mainloop()
