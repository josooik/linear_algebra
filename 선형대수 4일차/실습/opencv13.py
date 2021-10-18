# 이미지 확대(OpencCV resize 함수 사용)
import cv2
import numpy as np

img = cv2.imread('img/img3.jpg', cv2.IMREAD_COLOR)

# 이미지 사이즈 조정
img = cv2.resize(img, dsize=(400, 400), interpolation=cv2.INTER_AREA)

height, width = img.shape[:2]

# 이미지를 1.5배 확대합니다.
scale = 5.5
dst = cv2.resize(img, (int(width * scale), int(height * scale)))

cv2.imshow("result", dst)
cv2.waitKey(0)
