import pyautogui
import time


def youtube(name):
    print(pyautogui.position())
    pyautogui.click(927, 97)
    time.sleep(1)

    pyautogui.typewrite(name)
    pyautogui.press("enter")
    time.sleep(3)

    pyautogui.click(611, 230)

    