# warpAffine() 함수로 이미지 회전
import cv2
import numpy as np

img = cv2.imread('img/img1.jpg', cv2.IMREAD_COLOR)

# 이미지 사이즈 조정
img = cv2.resize(img, dsize=(800, 500), interpolation=cv2.INTER_AREA)

height, width = img.shape[:2]

angle = 45

center = (0, 0)

# getRotationMatrix2D 함수를 사용하여 angle만큼 회전하는 회전 변환 행렬을 생성합니다.
rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1)

# warpAffine 함수를 사용하여 회전 변환 행렬을 이미지에 적용합니다.
dst = cv2.warpAffine(img, rotation_matrix, (width, height))

result = cv2.hconcat([img, dst])
cv2.imshow("result", result)
cv2.waitKey(0)