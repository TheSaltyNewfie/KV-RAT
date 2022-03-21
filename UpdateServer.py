import socket
import os
from json import *

addr = "192.168.0.2"
port = 4455

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((addr, port))
server.listen(1)

version = "0.0.1"

while True:
    client, address = server.accept()
    print(f"Connection from {address[0]}:{address[1]}")

    msg = client.recv(1024)
    msg = msg.decode("utf-8")
    msg = msg.lower()

    if msg != version:
        client.send(f"OFD: Version - {version}")
        # send client updated files
    elif msg == version:
        client.send(f"UTD: Version - {version}")