# 회전 이미지 4개 출력
import cv2
import numpy as np

img = cv2.imread('img/img2.png', cv2.IMREAD_COLOR)

height, width = img.shape[:2]

angles = [0, 45, 90, 135]
dst = []

center_x = width / 2
center_y = height / 2

# getRotationMatrix2D 함수를 사용하여 angle만큼 회전하는 회전 변환 행렬을 생성합니다.

for i, angle in enumerate(angles):
    rotation_matrix = cv2.getRotationMatrix2D((center_x, center_y), angle, 1)
    dst.append(cv2.warpAffine(img, rotation_matrix, (width, height)))

    if i == 1:
        h1con = cv2.hconcat([dst[i-1], dst[i]])
    if i == 3:
        h2con = cv2.hconcat([dst[i-1], dst[i]])

result = cv2.vconcat([h1con, h2con])

cv2.imshow("result", result)
cv2.waitKey(0)