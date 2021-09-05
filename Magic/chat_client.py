import json
import socket
import threading
from tkinter import Tk, Label, Button

host = '192.168.1.206'
port = 55555
# SOCK_STREAM. AF_INET refers to the address-family ipv4. The SOCK_STREAM means connection-oriented TCP protocol.
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))

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
                print('msg recieved', msg)
                msgWindow = Tk()
                Label(msgWindow, text=msg).pack()

                def closewindow(event=''):
                    msgWindow.destroy()

                Button(msgWindow, command=closewindow)
                msgWindow.mainloop()
        except:
            print('An error occured')
            client.close()
            break


def sendtoserver(nickname, msg):
    try:
        msg = json.dumps((nickname, msg))
        client.send(msg.encode('ascii'))
    except:
        pass


def startclient():
    recievethread = threading.Thread(target=recievefromserver)
    recievethread.start()
