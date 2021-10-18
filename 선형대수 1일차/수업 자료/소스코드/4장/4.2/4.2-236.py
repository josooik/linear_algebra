import cv2
import numpy as np


img = cv2.imread('image.jpg', cv2.IMREAD_COLOR)
height,width = img.shape[:2]

angle = 45
center=(0,0)

# getRotationMatrix2D 함수를 사용하여 angle 만큼 회전하는 회전변환행렬을 생성합니다.
rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1)

# warpAffine 함수를 사용하여 회전변환행렬을 이미지에 적용합니다. 
dst = cv2.warpAffine(img, rotation_matrix, (width, height))


result = cv2.hconcat([img, dst]) 
cv2.imshow("result", result)
cv2.waitKey(0)
