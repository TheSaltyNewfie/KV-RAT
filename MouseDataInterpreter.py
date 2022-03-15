import win32api, win32con

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

    while timer < recordtime:
        win32api.GetCursorPos()

