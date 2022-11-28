import pyautogui
import time


def youtube(name):
    pyautogui.click(927, 97)
    time.sleep(1)

    pyautogui.typewrite(name)
    pyautogui.press("enter")
    time.sleep(3)

    pyautogui.click(611, 230)


def google(name):
    print(pyautogui.position())
    pyautogui.typewrite(name)
    pyautogui.press("enter")
    time.sleep(2)
    pyautogui.click(286, 292)

