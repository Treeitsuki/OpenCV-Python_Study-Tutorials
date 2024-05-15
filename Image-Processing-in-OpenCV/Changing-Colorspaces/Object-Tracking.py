import cv2
import numpy as np

cap = cv2.VideoCapture

while(1):
    #Take each frame
    _, frame = cap.read()
    
    #Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    #define range of blue color in HSV
    lower_bulue = np.asarray([110, 50, 50])
    upper_blue = np.asarray([130, 255, 255])
    
    
    #Threshold th HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower_bulue, upper_blue)

    #Bitwise-AND mask original image
    res = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()