import numpy as np
import cv2
import pyautogui, sys
import time
import keyboard


fata = [0,0]
spate = [0,0]
stanga = [0,0]
dreapta = [0,0]
stop = [0,0]

def define_region(aux):
    while True:
        if keyboard.is_pressed('space'):
            x, y = pyautogui.position() 
            positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
            print positionStr,
            print '\b' * (len(positionStr) + 2),
            aux[0] = x
            aux[1] = y
            break

define_region(fata)
