import win32api, win32com
import socket
import time
import mouse 

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
        msg = client.recv(1024)
        msg = msg.decode("utf-8")
        msg = msg.lower()

        cursorpos = mouse.get_position()
        lbtnA = mouse.is_pressed("left")
        rbtnA = mouse.is_pressed("right")
        
        
        if(msg == "callback"):
            csend(f'{str(cursorpos)}|{lbtnA}|{rbtnA}')
        

