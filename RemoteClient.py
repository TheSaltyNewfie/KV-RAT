# This just sends commands to the server to relay to the other client
import socket

addr = "127.0.0.1"
port = 4560

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect((addr, port))

def csend(message):
    server.send(bytes(message, "utf-8"))

try:
    while True:
        buffer = server.recv(1024)
        buffer = buffer.decode("utf-8")
        
        while True:
            userinput = input("Type Command => ")
            csend(userinput)
except Exception:
    print(f'Error: {Exception}')
