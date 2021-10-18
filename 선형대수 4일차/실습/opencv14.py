# 이미지 확대(OpencCV resize 함수 사용)
import cv2
import numpy as np

img = cv2.imread('img/img3.jpg', cv2.IMREAD_COLOR)

# 이미지 사이즈 조정
img = cv2.resize(img, dsize=(400, 400), interpolation=cv2.INTER_AREA)

scales = [0.3, 0.5, 0.7, 1]
dst = []

for i, scale in enumerate(scales):

    img_zeros = np.zeros_like(img, dtype=np.uint8)  # np.zeros_like() 함수는 검정 화면 출력
    tmp = cv2.resize(img, None, fx=scale, fy=scale) # scale값 만큼 이미지 크기 줄임
    height, width = tmp.shape[:2]  # resize()된 이미지 height, width 구함
    img_zeros[0 : height, 0 : width, :] = tmp
    dst.append(img_zeros)

    if i == 1:
        h1con = cv2.hconcat([dst[i - 1], dst[i]])

    if i == 3:
        h2con = cv2.hconcat([dst[i - 1], dst[i]])

result = cv2.vconcat([h1con, h2con])

cv2.imshow("result", result)
cv2.waitKey(0)