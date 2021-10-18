# 회전 이미지 8개 출력
import cv2
import numpy as np

img = cv2.imread('img/img3.jpg', cv2.IMREAD_COLOR)

# 이미지 사이즈 조정
img = cv2.resize(img, dsize=(400, 400), interpolation=cv2.INTER_AREA)

height, width = img.shape[:2]

angles = [0, 45, 90, 135, 180, 225, 270, 315]
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
    if i == 5:
        h3con = cv2.hconcat([dst[i-1], dst[i]])
    if i == 7:
        h4con = cv2.hconcat([dst[i-1], dst[i]])

result1 = cv2.vconcat([h1con, h2con])
result2 = cv2.vconcat([h3con, h4con])

result = cv2.hconcat([result1, result2])
cv2.imshow("result", result)
cv2.waitKey(0)