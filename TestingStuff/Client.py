import win32api, win32com
import socket
import mouse

addr = "192.168.0.2"
port = 4560

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect((addr, port))

while True:
    server.send(bytes("callback", "utf-8"))
    buffer = server.recv(1024)
    buffer = buffer.decode("utf-8")

    args = buffer.split("|")
    argsPOS = args[0].split(",")
    mx = str(argsPOS[0].strip("("))
    my = str(argsPOS[1].strip(")"))

    mouse.move(int(mx), int(my)) 
    if args[1] == "True":
        mouse.click("left")
    if args[2] == "True":
        mouse.click("right")



    '''
    print(f"{argd[0]} {argd[1]}")

    win32api.SetCursorPos(int(argd[0].strip("(")), int(argd[1].strip(")")))
    '''