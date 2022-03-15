import time
import socket
import random
import os

addr = "127.0.0.1"
port = 4560

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((addr, port))
server.listen(3)


def csend(message):
    client.send(bytes(message, "utf-8"))

isUserConnected = False

while True:
    client, address = server.accept()
    print(f"Connection from {address[0]}:{address[1]}")
    isUserConnected = True

    while isUserConnected:
        userinput = input("Type Command: ")
        try:
            csend(userinput)
            msg = client.recv(1024)
            msg = msg.decode("utf-8")
            msg = msg.lower()

            print(msg)
        except Exception as e:
            print(f"Error: {e}")
