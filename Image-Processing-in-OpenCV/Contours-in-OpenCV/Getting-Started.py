import numpy as np
import cv2

im = cv2.imread("test.jpg")
imgray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(imgray, 127, 255, 0)

img, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

#To draw all the contours in an image
cv2.drawContours(img, contours, -1, (0, 255, 0), 3)

#To draw an individual contour, say 4th contour 
cv2.drawContours(img, contours, 3, (0, 255, 0), 3)

#useful method
cnt = contours[4]
img = cv2.drawContours(img, [cnt], 0, (0, 255, 0), 3)