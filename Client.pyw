from platform import system
import socket
import pygame
import time
import win32api, win32con
import threading
import math
import os
import ctypes
import random
import sys
import argparse
import MouseDataInterpreter as mdi

#Initilizing things
#ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1) # Runs as admin
pygame.mixer.init()
addr = "127.0.0.1"
port = 4560

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect((addr, port))


def playAudio(audiopath = None, stopAudio = True):
    if stopAudio == False:
        pygame.mixer.music.load(audiopath)
        pygame.mixer.music.play()
    else:
        pygame.mixer.music.stop()

def returnmsg(msg):
    server.send(bytes(msg, "utf-8"))

def MoveMouse(x, y):
    x2 = 0
    y2 = 0

    nativeScreenSize = win32api.GetSystemMetrics(0), win32api.GetSystemMetrics(1)
    screenx = int(nativeScreenSize[0] / 2)
    screeny = int(nativeScreenSize[1] / 2)

    print(f'{nativeScreenSize[0]} {nativeScreenSize[1]} {screenx} {screeny}')

    win32api.SetCursorPos((screenx, screeny)) #This doesnt work for games

    while x2 < x:
        x2 = x2 + 16
        y2 = y2 + 9
        time.sleep(0.01)
        print(f'CursorX: {x2} CursorY: {y2}')
        win32api.SetCursorPos((x2, y2))

def bsod(videopath, waittime):
    os.startfile(videopath)
    time.sleep(waittime)
    print("BSOD STARTED")
    #os.system('powershell wininit')

def helpm():
    returnmsg("mm x y - This command moves the mouse in the set coords \naudio stop | audio audiopath - Either stops or plays audio \nmmr - Moves the mouse in a random spot \nbsod videopath waittime - plays a local video then bluescreens the computer \nexit - Closes the client")
    
#def autoMouse(mouseDataFile):
    

def returnScreenRes():
    res = win32api.GetSystemMetrics(0), win32api.GetSystemMetrics(1)
    return res

def parse(args):
    if args[0] == "audio":
        if args[1] == "stop":
            playAudio(True)
            returnmsg("Audio stopped")
        else:
            playAudio(args[1], False)
            returnmsg(f"Audio playing = {args[1]}")
    if args[0] == "mm":
        MoveMouse(int(args[1]), int(args[2]))
        returnmsg(f"Moving mouse to {args[1]}x{args[2]}")
    if args[0] == "mmr":
        MoveMouse(int(random.choice(returnScreenRes[0])), int(random.choice(returnScreenRes[1])))
        returnmsg("Random mouse movement started")
    if args[0] == "bsod":
        bsod(args[1], float(args[2]))
        returnmsg("Blue screen activated - Client will restart, restart server now")
    if args[0] == "help":
        helpm()
    if args[0] == "exit":
        returnmsg("Exiting - Start server soon")
        exit()
        
try:
    while True:
        buffer = server.recv(1024)
        buffer = buffer.decode("utf-8")

        splitargs = buffer.split()
        print(splitargs)

        parse(splitargs)
except Exception as e:
    print(f'Error: {e}')
    returnmsg(f"Error occured - Client closing \nMore Info: {e}")