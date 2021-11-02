# see https://www.youtube.com/watch?v=3UOyky9sEQY for a BASIC IDEA of how this works
import json
import socket
import threading

host, port, clients, nicknames = "127.0.0.1", 24094, [], []
# SOCK_STREAM. AF_INET refers to the address-family ipv4. The SOCK_STREAM means connection-oriented TCP protocol.
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()


def broadcast(username: str, message: str) -> None:
    """To send the message to a specific client"""
    try:
        print("Client found: ", client := clients[nicknames.index(username)], 'Msg send: ', message)
        client.send(message)
    except: print("No user found")


def handle(client: object) -> str:
    """Recieve data from a client"""
    while True:
        try:
            raw_message = client.recv(1024).decode("ascii")
            username, message = json.loads(raw_message)
            print("Broadcasting message to ", username)
            broadcast(username, message.encode("ascii"))
        except Exception as e:
            print(e, client, "not Functioning properly")
            # if error happens, remove the client
            # get the index to remove it from the nickname
            # the index for the client and nickname will be the same
            nicknames.pop(clients.index(client))  # Removing from nickname by getting the index of client
            clients.remove(client)
            client.close()
            del client
            break


def recieve() -> None:
    """To connect the client with the server"""
    while True:
        try:
            client, address = server.accept()
            print(f"connected with address: {address}")
            client.send("NICK".encode("ascii"))
            nickname = client.recv(1024).decode("ascii")
            nicknames.append(nickname)
            clients.append(client)
            print(f"{nickname} {address}")
            threading.Thread(target=handle, args=(client,)).start()
        except Exception as e:
            print(e)


def startserver() -> None:
    """To chat the start server"""
    print("Server has started")
    recieve()
if __name__ == '__main__':startserver()