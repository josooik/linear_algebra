# getRotationMatrix2D() 함수로 이미지 중심 회전
import cv2
import numpy as np

img = cv2.imread('img/img2.png', cv2.IMREAD_COLOR)
height, width = img.shape[:2]

angle = 45

center_x = width / 2
center_y = height / 2

# 좌표 (center_x, center_y)를 중심으로 angle만큼 회전하는 회전 변환 행령를 생성합니다.
rotation_matrix = cv2.getRotationMatrix2D((center_x, center_y), angle, 1)

# 이미지에 회전 변환 행렬을 적용합니다.
dst = cv2.warpAffine(img, rotation_matrix, (width, height))

result = cv2.hconcat([img, dst])
cv2.imshow("result", result)
cv2.waitKey(0)
