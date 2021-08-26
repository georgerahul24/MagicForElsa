from functools import partial
from tkinter import *
from tkinter import ttk
from tkinter.colorchooser import askcolor

from talk1.talk1 import talk

from Magic import tkinterlib, add_user, theme,history



def setting_page(event="", username='', state=True):
    """[GUI for the settings page]

    Args:
        event (str, optional): [Not important]. Defaults to "".
        username (str, optional): [Username of the user using the GUI]. Defaults to ''.
        state (bool, optional): [Not important]. Defaults to True.
    """

    def usr_page(event=''):
        talk('Please add a new user')
        add_user.user_page()

    settings = Tk()
    bg_colour, text_color, button_colour = theme.read_theme()
    tkinterlib.tkinter_initialise(settings,x=500,y=300)
    #...title bar...
    # for title bar refer https://stackoverflow.com/questions/23836000/can-i-change-the-title-bar-in-tkinter
    def move_window(event):
        settings.geometry(f'+{event.x_root}+{event.y_root}')
    title_bar = Frame(settings, bg=bg_colour, bd=4)
    title_bar.pack(fill="x")
    tab = ttk.Notebook(settings)
    #refer https://stackoverflow.com/questions/23038356/change-color-of-tab-header-in-ttk-notebook
    #slightly edited that
    #refer this https://www.pythontutorial.net/tkinter/ttk-style/ also
    noteStyle = ttk.Style()
    noteStyle.theme_use('default')
    noteStyle.configure("TNotebook", background=bg_colour, borderwidth=0,foreground=text_color)
    noteStyle.configure("TNotebook.Tab", background=button_colour, borderwidth=0,foreground=text_color)


    tab.pack(fill="both")
    # differnt frames for tabs
    settings_tab = Frame(settings, bg=bg_colour)
    theme_tab = Frame(settings, bg=bg_colour)
    history_tab = Frame(settings, bg=bg_colour)
    about_tab = Frame(settings, bg=bg_colour)
    # ...settings_tab......
    # ....add user.........
    adduser = Button(settings_tab,
                     text="Add User",
                     bd=0,
                     command=usr_page,
                     bg=bg_colour,
                     fg=text_color)
    adduser.pack(fill='x')
    # hover effect
    adduser.bind('<Enter>', partial(tkinterlib.on_enter, but=adduser))
    adduser.bind('<Leave>', partial(tkinterlib.on_leave, but=adduser))

    # ......theme tab..........

    def new_background_colour(event=''):
        color = askcolor()
        bg_colour, text_color, button_colour = theme.read_theme()
        if color[1] is not None:
            theme.theme_writer(color[1], text_color, button_colour)

    def font_colour(event=''):
        color = askcolor()
        bg_colour, text_color, button_colour = theme.read_theme()
        if color[1] is not None:
            theme.theme_writer(bg_colour, color[1], button_colour)

    def new_button_colour(event=''):
        color = askcolor()
        bg_colour, text_color, button_colour = theme.read_theme()
        if color[1] is not None:
            theme.theme_writer(bg_colour, text_color, color[1])

    background_colour = Button(theme_tab,
                               text="Background Colour",
                               bd=0,
                               bg=bg_colour,
                               fg=text_color,
                               command=new_background_colour)
    background_colour.pack(fill='x')
    background_colour.bind('<Enter>',
                           partial(tkinterlib.on_enter, but=background_colour))
    background_colour.bind('<Leave>',
                           partial(tkinterlib.on_leave, but=background_colour))

    new_text_colour = Button(theme_tab,
                             text="Font Colour",
                             bd=0,
                             bg=bg_colour,
                             fg=text_color,
                             command=font_colour)
    new_text_colour.pack(fill='x')
    new_text_colour.bind('<Enter>',
                         partial(tkinterlib.on_enter, but=new_text_colour))
    new_text_colour.bind('<Leave>',
                         partial(tkinterlib.on_leave, but=new_text_colour))

    new_button_colour = Button(theme_tab,
                               text="Button color",
                               bd=0,
                               bg=bg_colour,
                               fg=text_color,
                               command=new_button_colour)
    new_button_colour.pack(fil='x')
    new_button_colour.bind('<Enter>',
                           partial(tkinterlib.on_enter, but=new_button_colour))
    new_button_colour.bind('<Leave>',
                           partial(tkinterlib.on_leave, but=new_button_colour))
    #......Theme tab ends............
    #.......History tab starts.......

    showhis = Button(history_tab,
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
    clearhis = Button(history_tab,
                      text="Clear History",
                      bd=0,
                      bg=bg_colour,
                      fg=text_color,
                      command=lambda: history.clear_history(username))
    clearhis.pack(fill='x')
    # hover effect
    clearhis.bind('<Enter>', partial(tkinterlib.on_enter, but=clearhis))
    clearhis.bind('<Leave>', partial(tkinterlib.on_leave, but=clearhis))
    #...........history tab ends...........
    #...........about tab starts...........
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






    #Packing the tabs
    settings_tab.pack(fill='both')
    theme_tab.pack(fill='both')
    history_tab.pack(fill='both')
    about_tab.pack(fill='both')
    tab.add(settings_tab, text="Settings")
    tab.add(theme_tab, text="Theme")
    tab.add(history_tab, text="History")
    tab.add(about_tab, text="About")
    # ....close button....
    close = Button(title_bar,
                   text="x",
                   font='bold',
                   bd=0,
                   bg=bg_colour,
                   fg=text_color,
                   command=settings.destroy)
    close.pack(side=RIGHT)
    # hover effect
    close.bind('<Enter>', partial(tkinterlib.on_enter, but=close))
    close.bind('<Leave>', partial(tkinterlib.on_leave, but=close))
    #...moving titlebar...
    title_bar.bind('<B1-Motion>', move_window)
    settings.mainloop()



