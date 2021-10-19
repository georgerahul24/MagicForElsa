"""
This module is to display GUI for adding and deleting users
"""

from tkinter import Tk, Entry

from talk1.talk1 import talk

from Magic import file_database
from Magic.tkinterlib import TLabel, TButton, tkinter_initialise, TLabelFrame


def user_page():
    """[This function is used to implement the GUI of the add user page]"""
    userpage = Tk()
    tkinter_initialise(userpage, 600, 340)
    s = TLabelFrame(userpage, text="Add New User")
    s.grid(row=0, column=0)
    TLabel(s, text="Enter the username:").grid(row=0, column=0)
    TLabel(s, text="Enter the password:").grid(row=1, column=0)
    eu = Entry(s)
    eu.grid(row=0, column=1)
    ep = Entry(s)
    ep.grid(row=1, column=1)

    def add(event=""):
        """[Adds the user]"""
        new_user = eu.get()
        new_password = ep.get()
        state = file_database.write_to_file(new_user, new_password)
        if state == 1:
            talk(f"Successfully added {new_user}")

        elif state == -1:
            talk("user already exists. Try again")
        userpage.destroy()

    TButton(s, text="Add User", command=add).grid(row=3, column=1)
    TButton(s, text="X", command=userpage.destroy).grid(row=3, column=0)
    userpage.bind("<Return>", add)
    userpage.mainloop()


def deleteuser():
    """[This function is used to implement the GUI of the add user page]"""
    deleteuserpage = Tk()
    talk("Please enter the username and password to delete")
    tkinter_initialise(deleteuserpage, 600, 340)
    s = TLabelFrame(deleteuserpage, text="Delete User")
    s.grid(row=0, column=0)

    TLabel(s, text="Enter the username to delete:").grid(row=0, column=0)
    TLabel(s, text="Enter the password:").grid(row=1, column=0)
    TLabel(s, text="Retype the password:").grid(row=2, column=0)
    eu = Entry(s)
    ep = Entry(s)
    epr = Entry(s)
    eu.grid(row=0, column=1)
    ep.grid(row=1, column=1)
    epr.grid(row=2, column=1)

    def deleteuserfunc(event=""):
        """[Adds the user]"""
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

    TButton(s, text="Delete User", command=deleteuserfunc).grid(row=3, column=1)

    TButton(s, text="X", command=deleteuserpage.destroy).grid(row=3, column=0)

    deleteuserpage.bind("<Return>", deleteuserfunc)
    deleteuserpage.mainloop()
