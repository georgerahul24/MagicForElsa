'''Created by George Rahul
To simplify the pyttsx3 module'''
import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')  # getting details of current voice
# engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
engine.setProperty(
    'voice', voices[1].id)  # changing index, changes voices. 1 for female
rate = engine.getProperty('rate')  # getting details of current speaking rate
engine.setProperty('rate', 130)  # setting up new voice rate


def talk(speak):
    engine.say(speak)
    engine.runAndWait()
