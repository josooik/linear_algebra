# warpAffine() 함수로 이미지 이동 
import cv2
import numpy as np

img = cv2.imread('img/img1.jpg', cv2.IMREAD_COLOR)

# 이미지 사이즈 조정
img = cv2.resize(img, dsize=(800, 500), interpolation=cv2.INTER_AREA)

height, width = img.shape[:2]

M = np.array([[1, 0, 100], [0, 1, 200]], dtype=float)

# warpAffine 함수를 사용하여 이동 변환 행렬을 적용합니다.
dst = cv2.warpAffine(img, M, (width, height))

result = cv2.hconcat([img, dst])

cv2.imshow("result", result)
cv2.waitKey(0)