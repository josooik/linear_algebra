# 이미지 축소
import cv2
import numpy as np

img = cv2.imread('img/img3.jpg', cv2.IMREAD_COLOR)

# 이미지 사이즈 조정
img = cv2.resize(img, dsize=(400, 400), interpolation=cv2.INTER_AREA)

height, width = img.shape[:2]

# 0.5배 축소하는 변환 행렬을 생성합니다.
sclae_factor = 0.5
scaleing_matrix = np.array([[sclae_factor, 0, 0], [0, sclae_factor, 0], [0, 0, 1]])

dst = np.zeros((height, width, img.shape[2]), dtype=np.uint8)

for y in range(height):
    for x in range(width):

        new_p = np.array([x, y, 1])
        inv_scaling_matrix = np.linalg.inv(scaleing_matrix)
        old_p = np.dot(inv_scaling_matrix, new_p)

        x_, y_ = old_p[:2]
        x_ = int(x_)
        y_ = int(y_)

        if x_ > 0 and x_ < width and y_ > 0 and y_ < height:
            dst.itemset((y, x, 0), img.item(y_, x_, 0))  # blue 채널
            dst.itemset((y, x, 1), img.item(y_, x_, 1))  # green 채널
            dst.itemset((y, x, 2), img.item(y_, x_, 2))  # red 채널

cv2.imshow("result", dst)
cv2.waitKey(0)