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


while True:
    client, address = server.accept()
    print(f"Connection from {address[0]}:{address[1]}")

    while True:
        userinput = input("Type Command: ")
        csend(userinput)

