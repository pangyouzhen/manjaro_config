import pyautogui 
import keyboard
import time

currentMouseX, currentMouseY = pyautogui.position() # 鼠标当前位置
print(currentMouseX, currentMouseY)

while True:
    pyautogui.moveTo(100, 100, ) # 移动到 (100,100)
    pyautogui.moveTo(200, 100, )
    time.sleep(60)
