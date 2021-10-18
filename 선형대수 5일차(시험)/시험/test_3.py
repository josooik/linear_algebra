import cv2
import numpy as np

img = cv2.imread('img/img2.jpg', cv2.IMREAD_COLOR)

# 이미지 사이즈 조정
img = cv2.resize(img, dsize=(400, 400), interpolation=cv2.INTER_AREA)

height, width = img.shape[:2]

scales = [1, 0.7, 0.3]

dst = []

for i, scale in enumerate(scales):

    img_zeros = np.zeros_like(img, dtype=np.uint8)  # np.zeros_like() 함수는 검정 화면 출력
    tmp = cv2.resize(img, None, fx=scale, fy=scale)  # scale값 만큼 이미지 크기 줄임
    height, width = tmp.shape[:2]  # resize()된 이미지 height, width 구함
    img_zeros[0: height, 0: width, :] = tmp

    dst.append(img_zeros)

    if i == 2:
        h1con = cv2.hconcat([dst[i - 2], dst[i - 1]])
        h2con = cv2.hconcat([h1con, dst[i]])

cv2.imshow("result", h2con)
cv2.waitKey(0)