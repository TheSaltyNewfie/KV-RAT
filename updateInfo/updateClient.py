import socket
import os
import sys
import time

def checkUpdate():
    # This calls to the updateServer, then checks if an update is availble
    pass

def installUpdate():
    # This installs the update only, the way I will be doing it is very weird so it may not work
    pass

def verifyUpdate():
    # Just verifies the update for any inconsistancies with known good files
    pass

addr = "127.0.0.1"
port = 4455

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect((addr, port))

updateInstalled = False

while not updateInstalled:
    if checkUpdate():
        installUpdate()
        print("Update Installed fully, verifying...")
        if verifyUpdate():
            print("Client updated and verified")
        else:
            print("Client updated but missing files or corrupted files!")
