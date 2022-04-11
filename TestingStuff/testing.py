import win32api, win32com
import mouse

while True:
        cursorpos = mouse.get_position()
        mouseBtn = mouse.is_pressed("left")
        print(f"CursorPos: {cursorpos} MouseBtnActive: {mouseBtn}")