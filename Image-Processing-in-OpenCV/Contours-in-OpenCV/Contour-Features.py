import cv2
import numpy as np

img = cv2.imread("../../image/hand.jpg", 0)
ret, thresh = cv2.threshold(img, 127, 255, 0)
contours, hierarchy = cv2.findContours(thresh, 1, 2)

#Moment
cnt = contours[0]
M = cv2.moments(cnt)
print(M)

cx = int(M["m10"] / M["m00"])
cy = int(M["m01"] / M["m00"])

#Countor area
area = cv2.contourArea(cnt)

#Contour Perimeter  
perimeter = cv2.arcLength(cnt, True)

#Contour Approximation
epsilon = 0.1 * cv2.arcLength(cnt, True)
approx = cv2.approxPolyDP(cnt, epsilon, True)

#Convex Hull
hull = cv2.convexHull(cnt)

#Checking Convexity
k = cv2.isContourConvex(cnt)

#Bounding Rectangle
#(1)Straight Bounding Rectangle
x, y, w, h = cv2.boundingRect(cnt)
img = cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

#(2)Roated Rectangle
rect = cv2.minAreaRect(cnt)
box = cv2.boxPoints(rect)
bool = np.int0(box)
im = cv2.drawContours(img, [box], 0, (0, 0, 255), 2)

#Minimum Enclosing Circle
(x, y), radius = cv2.minEnclosingCircle(cnt)
center = (int(x), int(y))
radius = int(radius)
img = cv2.circle(img, center, radius, (0, 255, 0), 2)

#Fitting an Ellipse
ellipse = cv2.fitEllipse(cnt)
im = cv2.ellipse(im, ellipse, (0, 255, 0), 2)

#Fitting a Line
rows,cols = img.shape[:2]
[vx,vy,x,y] = cv2.fitLine(cnt, cv2.DIST_L2, 0, 0.01, 0.01)
lefty = int((-x*vy/vx) + y)
righty = int(((cols-x)*vy/vx)+y)
img = cv2.line(img,(cols-1,righty), (0,lefty), (0,255,0), 2)