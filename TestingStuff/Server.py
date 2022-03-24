import win32api, win32com
import socket

addr = "192.168.0.2"
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
        cursorpos = win32api.GetCursorPos()
        csend(str(cursorpos))