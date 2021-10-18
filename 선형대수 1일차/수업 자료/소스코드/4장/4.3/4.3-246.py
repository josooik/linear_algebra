import cv2
import numpy as np


img = cv2.imread('image.jpg', cv2.IMREAD_COLOR)
height,width = img.shape[:2]

# 이미지를 1.5배 확대합니다.
dst = cv2.resize(img, (int(width*1.5), int(height*1.5)));

cv2.imshow("result", dst)
cv2.waitKey(0)
