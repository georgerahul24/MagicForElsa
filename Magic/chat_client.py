import json
import socket
import threading
import win10toast
from Magic import export_import


def jsonenc(rec, data):
    """To convert the json data"""
    return json.dumps({"rec": rec, "data": data})


def jsondec(data: str) -> dict:
    """To convert the json data"""
    return json.loads(data)


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
    global client
    while True:
        try:
            msg = client.recv(1024).decode("ascii")
            rec = jsondec(msg)["rec"]
            match rec:
                case "Nick":
                    client.send(jsonenc("Nick", nickname).encode("ascii"))
                case "msg":
                    mesg = jsondec(msg)["data"]
                    print("msg received", mesg)
                    noti.show_toast("Elsa", mesg)
                    del msg, mesg, rec
        except Exception as e:
            print("Closing Connection", e)
            client.close()
            del client
            break


def sendtoserver(nickname: str, msg: str) -> None:
    """To send the data to the server"""
    try:
        print("Sending", msg, "to", nickname)
        client.send(jsonenc("msg", (nickname, msg)).encode("ascii"))
        del msg, nickname
    except: pass


def sendThemeToServer():
    data = (nickname, export_import.export('j'))
    client.send(jsonenc("sync", data).encode("ascii"))


def closeClient() -> None:
    """To close the connection of the client with the server"""
    client.close()


def startclient() -> None:
    """To start the process od connecting the client wth server"""
    client.connect((host, port))
    threading.Thread(target = recievefromserver).start()
