import cv2

#色変換の種類を指定するフラグ
flags = [i for i in dir(cv2) if i.startswith('COLOR_')]

print(flags)