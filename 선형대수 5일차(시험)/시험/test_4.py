import cv2
import numpy as np

img = cv2.imread('img/img3.jpg', cv2.IMREAD_COLOR)

# 이미지 사이즈 조정
img = cv2.resize(img, dsize=(400, 400), interpolation=cv2.INTER_AREA)

height, width = img.shape[:2]
scale = 0.5
angles = [0, 60, 120, 180, 240, 300]

center_x = width / 2
center_y = height / 2

dt = []

for i, angle in enumerate(angles):
    rotation_matrix = cv2.getRotationMatrix2D((center_x, center_y), angle, 1)
    dt1 = cv2.warpAffine(img, rotation_matrix, (0, 0))

    dt.append(dt1)

    if i == 2:
        h1con = cv2.hconcat([dt[i - 2], dt[i - 1]])
        h1con_1 = cv2.hconcat([h1con, dt[i]])

    if i == 5:
        h2con = cv2.hconcat([dt[i - 2], dt[i - 1]])
        h2con_2 = cv2.hconcat([h2con, dt[i]])

result = cv2.vconcat([h1con_1, h2con_2])
cv2.imshow("result", result)
cv2.waitKey(0)
cv2.destroyAllWindows()