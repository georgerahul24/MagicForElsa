import json
import socket
import threading

import win10toast

noti = win10toast.ToastNotifier()
host, port, nickname = "127.0.0.1", 24094, ""
# SOCK_STREAM. AF_INET  -> address-family ipv4 & SOCK_STREAM -> TCP protocol(see geek for geeks)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def getNickname(name: str) -> str:
    """To get the nickname i.e the username of the client"""
    global nickname
    nickname = name


def recievefromserver() -> None:
    """To receive data from the server"""
    while True:
        try:
            if (msg := client.recv(1024).decode("ascii")) == "NICK":
                client.send(nickname.encode("ascii"))
            else:
                print("msg recieved", msg)
                noti.show_toast("Elsa", msg)
                del msg
        except Exception as e:
            print("Closing Connection", e)
            client.close()
            del client
            break


def sendtoserver(nickname: str, msg: str) -> None:
    """To send the data to the server"""
    try:
        print("Sending", msg, "to", nickname)
        client.send(json.dumps((nickname, msg)).encode("ascii"))
        del msg, nickname
    except:pass


def closeClient() -> None:
    """To close the connection of the client with the server"""
    client.close()


def startclient() -> None:
    """To start the process od connecting the client wth server"""
    client.connect((host, port))
    threading.Thread(target=recievefromserver).start()
