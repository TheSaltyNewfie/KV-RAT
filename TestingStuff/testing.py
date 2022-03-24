import win32api, win32com

while True:
        cursorpos = win32api.GetCursorPos()
        print(cursorpos)