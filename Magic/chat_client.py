import gc
import json
import socket
import threading
import win10toast

noti = win10toast.ToastNotifier()

host = "127.0.0.1"
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
            msg = client.recv(1024).decode("ascii")
            if msg == "NICK":
                client.send(nickname.encode("ascii"))
            else:
                print("msg recieved", msg)
                noti.show_toast("Elsa", msg)
                del msg
                gc.collect()

        except:
            print("Closing Connection")
            client.close()
            gc.collect()
            break


def sendtoserver(nickname, msg):
    try:
        print("Sending", msg, "to", nickname)
        msg = json.dumps((nickname, msg))
        client.send(msg.encode("ascii"))
        del msg, nickname
        gc.collect()

    except:
        pass


def closeClient():
    client.close()


def startclient():
    client.connect((host, port))
    recievethread = threading.Thread(target=recievefromserver)
    recievethread.start()
