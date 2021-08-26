from tkinter import Tk, LabelFrame, Button
import os


def read_theme():
    """[Reads the theme from the initial.elsa file]

    Returns:
        [bg_colour,text_colour,button_colour]: [The background,text/font and the button colour found]
    """
    try:
        initpth = os.getcwd() + '\\resources\\ initial.elsa'
        f = open(initpth)
        datas = f.read()
        colours = datas.split(';')
        bg_colour = colours[0].rstrip().lstrip()
        text_color = colours[1].rstrip().lstrip()
        colours = colours[2].split('\n')

        button_colour = colours[0].rstrip().lstrip()
        return bg_colour, text_color, button_colour
    except Exception as e:
        print('initial.elsa is corrupted')
        print(e)


def theme_writer(bg_colour, font_colour, button_colour):
    initpth = os.getcwd() + '\\resources\\ initial.elsa'
    f = open(initpth, 'w')
    f.write(
        f"{bg_colour};{font_colour};{button_colour}\n #The order is bg,font color,button colour \n#Please remember to use ';' to separate colours :D"
    )
    f.close()

#...............no need for this function......
#...............This function is implemeneted in the settings page.......
def theme_selector(event=''):
    """[GUI to select a new theme]

    Args:
        event (str, optional): [Not important]. Defaults to ''.
    """
    from tkinter.colorchooser import askcolor
    from Magic import tkinterlib
    from functools import partial

    bg_colour, text_color, button_colour = read_theme()

    selectorpage = Tk()
    tkinterlib.tkinter_initialise(selectorpage, 600, 340, top=0)
    selector = LabelFrame(selectorpage,
                          text="Theme",
                          bg=bg_colour,
                          fg=text_color)
    selector.pack()

    def new_background_colour(event=''):
        color = askcolor()
        bg_colour, text_color, button_colour = read_theme()
        if color[1] != None:
            theme_writer(color[1], text_color, button_colour)

    def font_colour(event=''):
        color = askcolor()
        bg_colour, text_color, button_colour = read_theme()
        if color[1] != None:
            theme_writer(bg_colour, color[1], button_colour)

    def new_button_colour(event=''):
        color = askcolor()
        bg_colour, text_color, button_colour = read_theme()
        if color[1] != None:
            theme_writer(bg_colour, text_color, color[1])

    background_colour = Button(selector,
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

    new_text_colour = Button(selector,
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

    new_button_colour = Button(selector,
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

    close = Button(selectorpage,
                   text="x",
                   font='bold',
                   bd=0,
                   bg=bg_colour,
                   fg=text_color,
                   command=selectorpage.destroy)
    close.pack()

    close.bind('<Enter>', partial(tkinterlib.on_enter, but=close))
    close.bind('<Leave>', partial(tkinterlib.on_leave, but=close))
    selectorpage.mainloop()
