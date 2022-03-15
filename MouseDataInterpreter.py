import win32api, win32con

def readIMD(mouseData):
    #Reads the file and translates it to actually readable numbers
    NonSort = []
    XList = []
    YList = []
    with open(mouseData, 'rb') as mdata:
        NonSort = mdata.readlines().split()

        for element in NonSort:
            XList = any('X' in element)
            YList = any('Y' in element)

