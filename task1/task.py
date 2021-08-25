'''Created by George Rahul
Contains all the necessary code to run various features'''
import pyttsx3, datetime, subprocess, webbrowser, random, os
from pathlib import Path
from talk1 import talk1
talk=talk1.talk


# .....Time and Greeting............
def greeting(nam):
    try:
        x = datetime.datetime.now().hour

        if x < 12:
            talk(f"Good morning {nam}")
        else:
            talk(f"Good evening {nam}")
    except:
        print("Sorry i couldnt do what you requested Try again later")


def tell_time():
    talk(f"It is {datetime.datetime.now().hour} hours")


# ...........Programmes..........................
def wordpad():
    try:
        subprocess.Popen('C:\\Windows\\System32\\write.exe')
        talk(f"I have opened wordpad for you")
    except:
        print("Sorry i couldnt do what you requested Try again later")


def whatsapp():
    try:

        subprocess.Popen(
            os.path.join(os.path.join(os.environ['USERPROFILE']),
                         'AppData\\Local\\WhatsApp\\WhatsApp.exe'))
        print("Opened WhatsApp")
        talk(f"I have opened whatsapp for you")

    except Exception as e:
        print(e, "Sorry i couldnt do what you requested Try again later")


def gimp():
    try:
        subprocess.Popen("C:\\Program Files\\GIMP 2\\bin\\gimp-2.10.exe")
        talk("I have opened gimp for you")
    except:
        talk("Sorry i could not open gimp ")


def firefox():
    try:
        subprocess.Popen('C:\\Program Files\\Mozilla Firefox\\firefox.exe')
        talk("i have opened firefox for you")
    except Exception as e:
        talk("Sorry, could not open firefox")
        print("Sorry i couldnt do what you requested Try again later", e)


def photoshop():
    try:
        os.system('photoshop')
        talk("i have opened photoshop for you")
    except Exception as e:
        talk("Sorry, could not open photoshop")
        print("Sorry i couldnt do what you requested Try again later", e)


def vscode():
    try:
        os.system('code')
        talk("i have opened visual studio code for you")
    except Exception as e:
        talk("Sorry, could not open visual studio code")
        print("Sorry i couldnt do what you requested Try again later", e)


def vlc():
    try:
        os.system('vlc')
        talk("i have opened vlc for you")
    except Exception as e:
        talk("Sorry, could not open vlc")
        print("Sorry i couldnt do what you requested Try again later", e)


def telegram():
    try:
        os.system('telegram')
        talk("i have opened telegram for you")
    except Exception as e:
        talk("Sorry, could not open telegram ")
        print("Sorry i couldnt do what you requested Try again later", e)


def powerpoint():
    try:
        os.system('powerpnt')
        talk("i have opened powerpoint for you")
    except Exception as e:
        talk("Sorry, could not open powerpoint ")
        print("Sorry i couldnt do what you requested Try again later", e)


def msword():
    try:
        os.system('winword')
        talk("i have opened word for you")
    except Exception as e:
        talk("Sorry, could not open word")
        print("Sorry i couldnt do what you requested Try again later", e)


# .........browser and net related................
def web(a):
    try:
        searchword = a
        webbrowser.open('https://www.google.com/search?client=firefox-b-d&q=' +
                        searchword,
                        new=1)
        talk(f"This is what I found for {a}")
    except:
        webbrowser.open(webbrowser.open(searchword, new=1))
        print("Sorry i couldnt do what you requested Try again later")


def youtube(srch):
    webbrowser.open(f"https://www.youtube.com/results?search_query={srch}")
    talk(f"Here is what you requested")


# .............folders......................
def download():
    try:
        os.startfile(
            Path(
                os.path.join(os.path.join(os.environ['USERPROFILE']),
                             'Downloads')))
        talk(f"Here is what you requested")
    except:
        talk("Sorry, could not open the downloads folder")
        print("Sorry i couldnt do what you requested Try again later")


def desktop():
    try:
        os.startfile(
            Path(
                os.path.join(os.path.join(os.environ['USERPROFILE']),
                             'Desktop')))
        talk(f"Here is what you requested")
    except:
        talk("Sorry, could not open the desktop folder")
        print("Sorry i couldnt do what you requested Try again later")


def musicFolder():
    try:
        os.startfile(
            Path(os.path.join(os.path.join(os.environ['USERPROFILE']),
                              'Music')))
        talk(f"Here is what you requested")
    except:
        talk("Sorry, could not open the Music folder")
        print("Sorry i couldnt do what you requested Try again later")


def desktop():
    try:
        os.startfile(
            Path(
                os.path.join(os.path.join(os.environ['USERPROFILE']),
                             'Desktop')))
        talk(f"Here is what you requested")
    except:
        talk("Sorry, could not open the downloads folder")
        print("Sorry i couldnt do what you requested Try again later")


def joke():
    try:
        jokeslist = [
            'My friend was explaining electricity to me, but I was like, wat ?',
            'I failed math so many times at school, I can’t even count',
            'Never trust atoms; they make up everything', 'George is a fool',
            'The future, the present, and the past walk into a bar. Things got a little tense',
            'It was an emotional wedding. Even the cake was in tiers'
        ]
        jokeselected = random.choice(jokeslist)
        talk(jokeselected)
    except:
        talk('Let me think. please try again')


#...........shutdown,restart and log off.....
def shutdown():
    try:
        #/s is for shutdown and 15 is for a 15 seconds delay when shutdowning
        talk("Shutting down your computer in 15 seconds. Bye bye")
        subprocess.call(["shutdown", '/s', '/t', "15"])
    except:
        talk("Sorry.Something went wrong")


def restart():
    try:
        #/r is for restart and 15 is for a 15 seconds delay when shutdowning
        talk("Restarting your computer in 15 seconds. Bye bye")
        subprocess.call(["shutdown", '/r', '/t', "15"])
    except:
        talk("Sorry.Something went wrong")
