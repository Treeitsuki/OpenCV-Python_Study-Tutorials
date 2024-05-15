import cv2
import numpy as np

img = cv2.imread("j.png", 0)
kernel = np.ones((5, 5), np.uint8)
erosion = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)

cv2.imshow("img", erosion)
cv2.waitKey(0)
cv2.destroyAllWindows()