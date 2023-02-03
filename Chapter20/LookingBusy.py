import pyautogui
import time

#print(pyautogui.mouseInfo())

print('Ctrl+C to end the program')

try:
    while True:
        #duration = 0.5s
        pyautogui.moveRel(10, 0, 0.5)
        pyautogui.moveRel(-10, 0, 0.5)
        time.sleep(10)

except KeyboardInterrupt:
    print('Deactivated')

    