"""
This module contains the GUI for settings
"""
import os
from functools import partial
from tkinter import Tk, Frame, Label, LabelFrame, RIGHT
from tkinter import ttk
from tkinter.colorchooser import askcolor
from tkinter.filedialog import askdirectory

from talk1.talk1 import talk

from Magic import usergui, theme, history, indexer, export_import, popups, tkinterlib
from Magic.tkinterlib import TButton


def setting_page(event="", username="", state=True):
    """[GUI for the settings page]

    Args:
        event (str, optional): [Not important]. Defaults to "".
        username (str, optional): [Username of the user using the GUI]. Defaults to ''.
        state (bool, optional): [Not important]. Defaults to True.
    """
    def usr_page(event=""):
        talk("Please add a new user")
        usergui.user_page()

    settings = Tk()
    bg_colour, text_color, button_colour = theme.read_theme()
    tkinterlib.tkinter_initialise(settings, x=500, y=300, top=0)

    # ...title bar...
    # for title bar refer https://stackoverflow.com/questions/23836000/can-i-change-the-title-bar-in-tkinter
    def move_window(event):
        settings.geometry(f"+{event.x_root}+{event.y_root}")

    title_bar = Frame(settings, bg=bg_colour, bd=4)
    title_bar.pack(fill="x")
    tab = ttk.Notebook(settings)
    tab.pack(fill="both")
    # differnt frames for tabs
    settings_tab = Frame(settings, bg=bg_colour)
    theme_tab = Frame(settings, bg=bg_colour)
    history_tab = Frame(settings, bg=bg_colour)
    about_tab = Frame(settings, bg=bg_colour)
    indexer_tab = Frame(settings, bg=bg_colour)
    # ...settings_tab......
    # ....add user.........
    adduser = TButton(
        settings_tab,
        text="Add User",
        command=usr_page,
    )
    adduser.pack(fill="x")
    # hover effect

    # .....delete a user............
    deleteusr = TButton(
        settings_tab,
        text="Delete User",
        command=usergui.deleteuser,
    )
    deleteusr.pack(fill="x")

    # .....reset vira............
    reset = TButton(
        settings_tab,
        text="Reset Elsa",
        command=popups.resetelsapopup,
    )
    reset.pack(fill="x")

    # ...import export themes.....
    # ....Export data...........
    exportdata = TButton(
        settings_tab,
        text="Export Data",
        command=export_import.export,
    )
    exportdata.pack(fill="x")

    # .......import data......
    importdata = TButton(
        settings_tab,
        text="Import Data",
        command=export_import.import_data,
    )
    importdata.pack(fill="x")

    # hover effect

    # ......theme tab..........

    def new_background_colour(event=""):
        color = askcolor()
        bg_colour, text_color, button_colour = theme.read_theme()
        if color[1] is not None:
            theme.theme_writer(color[1], text_color, button_colour)

    def font_colour(event=""):
        color = askcolor()
        bg_colour, text_color, button_colour = theme.read_theme()
        if color[1] is not None:
            theme.theme_writer(bg_colour, color[1], button_colour)

    def new_button_colour(event=""):
        color = askcolor()
        bg_colour, text_color, button_colour = theme.read_theme()
        if color[1] is not None:
            theme.theme_writer(bg_colour, text_color, color[1])

    background_colour = TButton(
        theme_tab,
        text="Background Colour",
        command=new_background_colour,
    )
    background_colour.pack(fill="x")

    new_text_colour = TButton(
        theme_tab,
        text="Font Colour",
        command=font_colour,
    )
    new_text_colour.pack(fill="x")

    new_button_colour = TButton(
        theme_tab,
        text="Button color",
        command=new_button_colour,
    )
    new_button_colour.pack(fil="x")

    # ......Theme tab ends............
    # .......History tab starts.......

    showhis = TButton(
        history_tab,
        text="Show History",
        command=partial(history.user_read, username=username),
    )

    showhis.pack(fill="x")

    # clear history button
    clearhis = TButton(
        history_tab,
        text="Clear History",
        command=lambda: history.clear_history(username),
    )
    clearhis.pack(fill="x")

    # ...........history tab ends...........
    # ...........about tab starts...........
    version = LabelFrame(about_tab,
                         text="Version",
                         bg=bg_colour,
                         fg=text_color)
    verlabel = Label(version, text="Elsa 1.1", bg=bg_colour, fg=text_color)
    verlabel.pack()
    version.pack()

    ab = LabelFrame(about_tab, text="Created By", bg=bg_colour, fg=text_color)
    ab.pack()
    # Name labels
    a = Label(ab, text="Austin Bert", bg=bg_colour, fg=text_color).pack()
    e = Label(ab, text="Elizabeth Jaison", bg=bg_colour, fg=text_color).pack()
    g = Label(ab, text="George Rahul", bg=bg_colour, fg=text_color).pack()

    # .........indexer tab.............
    def folderlabels():
        try:
            folders = indexer.read_indexer_folders()
            for folder in folders:
                foldername = folder.split("/")[-1]
                Label(indexer_tab,
                      text=foldername,
                      bg=bg_colour,
                      fg=text_color).pack()
        except:
            pass
        del folders

    def folderchooser():
        folderpath = askdirectory()
        indexer.add_indexer_folders(path=folderpath)
        settings.destroy()
        setting_page()
        del folderpath

    indexerbutton = TButton(
        indexer_tab,
        text="Add a folder",
        command=folderchooser,
    )
    indexerbutton.pack()

    # ....Reset indexerparthlib.....
    def resetindexercache():
        talk("Reseted the cache")
        os.remove((os.getcwd() + "\\resources\\ indexer.elsa"))
        print("'indexer.elsa' is removed")

    resetindexerpathlib = TButton(
        indexer_tab,
        text="Reset Indexer Cache",
        command=resetindexercache,
    )
    resetindexerpathlib.pack()
    # hover effect

    indexertitle = Label(
        indexer_tab,
        text="Additional Indexed folders",
        font="bold",
        bg=bg_colour,
        fg=text_color,
    )
    indexertitle.pack()
    folderlabels()
    # Packing the tabs
    settings_tab.pack(fill="both")
    theme_tab.pack(fill="both")
    history_tab.pack(fill="both")
    about_tab.pack(fill="both")
    indexer_tab.pack(fill="both")
    tab.add(settings_tab, text="Settings")
    tab.add(theme_tab, text="Theme")
    tab.add(history_tab, text="History")
    tab.add(about_tab, text="About")
    tab.add(indexer_tab, text="Indexer")

    # ....close button....
    def quitsettings(event=""):
        settings.destroy()
        indexer.index_files()

    close = TButton(
        title_bar,
        text="x",
        command=quitsettings,
    )
    close.pack(side=RIGHT)

    # ...moving titlebar...
    title_bar.bind("<B1-Motion>", move_window)
    settings.mainloop()
