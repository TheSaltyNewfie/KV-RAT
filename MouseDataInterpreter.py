import win32api, win32con
import time

def readIMD(mouseData):
    '''
    Insert a file that contains mouse data, it will convert it to a list that can be properly read by other code
    '''
    XList = []
    YList = []
    NonSort = []
    NonSort = mouseData.readlines().split()
    for element in NonSort:
        if element.startswith('X'):
            XList.append(element)
        else:
            YList.append(element)
    return XList, YList

def setIMD(mouseData, recordtime):
    '''
    This records data from the mouse, can be used to do funny shapes
    '''
    timer = 0
    ox = 0
    oy = 0

    while timer < recordtime:
        ox, oy = win32api.GetCursorPos()
        print(f'X{ox} Y{oy}\n', file=mouseData)
        timer = timer + 1
        time.sleep(0.1)

def runIMD(mouseData):
    for xv in mouseData[0]:
        for yv in mouseData[1]:
            win32api.SetMousePos((xv, yv))