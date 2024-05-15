import cv2
import numpy as np

#画像の読み込み
img = cv2.imread("lena.png")

#画素値にアクセス
px = img[100, 100]
print(px)

#画素値（青）
blue = img[100, 100, 0]
print(blue)

#画素数の変更
img[100, 100] = [255, 255, 255]
print(img[100, 100])

#accessing RED value
img.item(10, 10, 2)

#modifying RED value