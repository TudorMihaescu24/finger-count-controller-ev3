import numpy as np
import cv2
import pyautogui, sys
import keyboard
import time

fata = [0,0]
spate = [0,0]
stanga = [0,0]
dreapta = [0,0]
stop = [0,0]


def define_region(aux):
    while True:
        if keyboard.is_pressed('space'):
            x, y = pyautogui.position() 
            aux[0] = x
            aux[1] = y
            break           

def click():
    print("Puncte fata:")
    define_region(fata)
    time.sleep(1)
    print("Puncte spate:")
    define_region(spate)
    time.sleep(1)
    print("Puncte stanga:")
    define_region(stanga)
    time.sleep(1)
    print("Puncte dreapta:")
    define_region(dreapta)
    time.sleep(1)
    print("Puncte stop:")
    define_region(stop)
    time.sleep(1)
         


def color_detection(img):
    hsvim = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower = np.array([110, 50, 50], dtype="uint8")
    upper = np.array([130, 255, 255], dtype="uint8")
    glovecolorHSV = cv2.inRange(hsvim, lower, upper)
    blurred = cv2.blur(glovecolorHSV, (2, 2))
    ret, thresh = cv2.threshold(blurred, 30, 255, cv2.THRESH_BINARY)
    return thresh


def contours_generator(test_img):
    contours, hierarchy = cv2.findContours(
        test_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = max(contours, key=lambda x: cv2.contourArea(x))
    hull = cv2.convexHull(contours)
    return contours, hull


def defects_finder(contours):
    hull = cv2.convexHull(contours, returnPoints=False)
    defects = cv2.convexityDefects(contours, hull)
    return defects


def hand(img):
    try:
        test_img = color_detection(img)
        contours, hull = contours_generator(test_img)
        cv2.drawContours(img, [contours], -1, (255, 255, 0), 2)
        cv2.drawContours(img, [hull], -1, (0, 255, 255), 2)
        defects = defects_finder(contours)
        if defects is not None:
            cnt = 0
            for i in range(defects.shape[0]):
                s, e, f, d = defects[i][0]
                start = tuple(contours[s][0])
                end = tuple(contours[e][0])
                far = tuple(contours[f][0])
                a = np.sqrt((end[0] - start[0]) ** 2 + (end[1] - start[1]) ** 2)
                b = np.sqrt((far[0] - start[0]) ** 2 + (far[1] - start[1]) ** 2)
                c = np.sqrt((end[0] - far[0]) ** 2 + (end[1] - far[1]) ** 2)
                angle = np.arccos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c))  
                if angle <= np.pi / 2:
                    cnt += 1
                    cv2.circle(img, far, 4, [0, 0, 255], -1)
            if(cnt == 0):
                pyautogui.click(stop[0],stop[1])
                time.sleep(0.1)
            elif(cnt == 1):
                pyautogui.click(fata[0],fata[1])
                time.sleep(0.1)
            elif(cnt == 2):
                pyautogui.click(stanga[0],stanga[1])
                time.sleep(0.1)
            elif(cnt == 3):
                pyautogui.click(dreapta[0],dreapta[1])
                time.sleep(0.1)
            elif(cnt == 4):
                pyautogui.click(spate[0],spate[1])
                time.sleep(0.1)
            cv2.putText(frame, str(cnt+1), (0, 50), cv2.FONT_HERSHEY_SIMPLEX,1, (255, 0, 0), 2, cv2.LINE_AA)   
        return img
    except:
        return img

cap = cv2.VideoCapture(0)
upper_left = (50, 50)
bottom_right = (450, 450)
click()
while cap.isOpened():
    ret, frame = cap.read()
    r = cv2.rectangle(frame, upper_left, bottom_right, (255, 255, 255), 2)
    ROI = frame[upper_left[1] : bottom_right[1], upper_left[0] : bottom_right[0]]
    cv2.imshow('pixelated_ROI', hand(ROI) )
    cv2.imshow('webcam', frame )
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
