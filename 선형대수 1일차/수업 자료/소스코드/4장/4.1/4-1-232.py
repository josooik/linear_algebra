import cv2
import numpy as np


img = cv2.imread('image.jpg', cv2.IMREAD_COLOR)
height,width = img.shape[:2]

M = np.array([[1, 0, 100], [0, 1, 200]], dtype=float)

# warpAffine 함수를 사용하여 이동 변환 행렬을 적용합니다. 
dst = cv2.warpAffine(img, M, (width, height))

result = cv2.hconcat([img, dst])

cv2.imshow("result", result)
cv2.waitKey(0)
