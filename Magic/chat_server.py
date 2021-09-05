# see https://www.youtube.com/watch?v=3UOyky9sEQY
import socket
import threading
import json

host = '127.0.0.1'
port = 24094
# SOCK_STREAM. AF_INET refers to the address-family ipv4. The SOCK_STREAM means connection-oriented TCP protocol.
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))

server.listen()

clients = []
nicknames = []


def broadcast(username, message):
    try:
        index = nicknames.index(username)
        print("Index of user:", index)
        client = clients[index]
        print("Client found", client)
        client.send(message)
        print(message)
    except:
        print("No user found")


def handle(client):
    while True:
        try:
            raw_message = client.recv(1024).decode('ascii')
            username, message = json.loads(raw_message)
            print(username)
            print("Broadcasting message")
            broadcast(username, message.encode('ascii'))
        except Exception as e:
            print(e)
            # if error happens, remove the client
            # get the index to remove it from the nickname
            # the index for the client and nickname will be the same
            print(client, "not Functioning properly")
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]

            broadcast(f'{nickname} left the chat !'.encode('ascii'))
            nicknames.remove(nickname)
            break


def recieve():
    while True:
        client, address = server.accept()
        print(f"connected with address: {address}")
        client.send('NICK'.encode('ascii'))
        nickname = client.recv(1024).decode('ascii')
        nicknames.append(nickname)
        clients.append(client)
        print(f"{nickname} {address}")
        thread = threading.Thread(target=handle, args=(client, ))
        thread.start()


print('Server has started')
recieve()
