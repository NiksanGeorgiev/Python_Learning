import pyautogui as pg
from time import sleep
from pynput.keyboard import Key, Controller

keyboard = Controller()
sleep(2)  
pg.click(1695,67)
sleep(2)
pg.click(1600,250)
sleep(1)
pg.click(1450,320)
sleep(1)
pg.click(26,258)
sleep(1)
pg.click(450,1055)
sleep(1)
with keyboard.pressed(Key.ctrl):
    keyboard.press('v')
    keyboard.release('v')
keyboard.press(Key.enter)
keyboard.release(Key.enter)