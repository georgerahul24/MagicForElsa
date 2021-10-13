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


def getNickname(name: str) -> str:
    """To get the nickname i.e the username of the client"""
    global nickname
    nickname = name


def recievefromserver() -> None:
    """To recieve data from the server"""
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


def sendtoserver(nickname: str, msg: str) -> None:
    """To send the data to the server"""
    try:
        print("Sending", msg, "to", nickname)
        msg = json.dumps((nickname, msg))
        client.send(msg.encode("ascii"))
        del msg, nickname
        gc.collect()

    except:
        pass


def closeClient() -> None:
    """To close the connection of the client with the server"""
    client.close()


def startclient() -> None:
    """To start the process od connecting the client wth server"""
    client.connect((host, port))
    recievethread = threading.Thread(target=recievefromserver)
    recievethread.start()
