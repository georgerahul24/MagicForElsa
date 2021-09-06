import json
import socket
import threading
from tkinter import Tk, Label, Button
import gc

host = '127.0.0.1'
port = 24094
# SOCK_STREAM. AF_INET refers to the address-family ipv4. The SOCK_STREAM means connection-oriented TCP protocol.(geek for geeks)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

nickname = ""


def getNickname(name):
    global nickname
    nickname = name


def recievefromserver():
    while True:
        try:
            msg = client.recv(1024).decode('ascii')
            if msg == "NICK":
                client.send(nickname.encode('ascii'))
            else:
                gc.disable()
                print('msg recieved', msg)
                msgWindow = Tk()
                Label(msgWindow, text=msg).pack()

                def closewindow(event=''):
                    msgWindow.destroy()
                    del msgWindow

                msgWindow.mainloop()

                gc.enable()
        except:
            print('Closing Connection')
            client.close()
            break


def sendtoserver(nickname, msg):
    try:
        print("Sending", msg, "to", nickname)
        msg = json.dumps((nickname, msg))
        client.send(msg.encode('ascii'))
        print("GC", gc.isenabled())
    except:
        pass


def closeClient():
    client.close()


def startclient():
    client.connect((host, port))
    recievethread = threading.Thread(target=recievefromserver)
    recievethread.start()
