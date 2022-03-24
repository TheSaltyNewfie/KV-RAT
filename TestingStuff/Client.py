import win32api, win32com
import socket

addr = "192.168.0.2"
port = 4560

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect((addr, port))

while True:
    buffer = server.recv(1024)
    buffer = buffer.decode("utf-8")

    argd = buffer.split(",")
    
    print(f"{argd[0]} {argd[1]}")

    #win32api.SetCursorPos(int(argd[0].strip("(")), int(argd[1].strip(")")))