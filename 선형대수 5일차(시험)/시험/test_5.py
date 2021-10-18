import cv2
import numpy as np

img = cv2.imread('img/img4.jpg', cv2.IMREAD_COLOR)

# 이미지 사이즈 조정
img = cv2.resize(img, dsize=(400, 400), interpolation=cv2.INTER_AREA)

height, width = img.shape[:2]

scales = [1, 0.7, 0.7, 0.7]
angles = [0, 0, 0, 45]

center_x = width / 2
center_y = height / 2

dst = []
dst_1 = []
dst1 = []

for i, scale in enumerate(scales):

    img_zeros = np.zeros_like(img, dtype=np.uint8)  # np.zeros_like() 함수는 검정 화면 출력
    tmp = cv2.resize(img, None, fx=scale, fy=scale)  # scale값 만큼 이미지 크기 줄임
    height, width = tmp.shape[:2]  # resize()된 이미지 height, width 구함
    img_zeros[0: height, 0: width, :] = tmp

    dst.append(img_zeros)

    if i == 1:
        h1con = cv2.hconcat([dst[i - 1], dst[i]])

    if i == 2:
        M = np.array([[1, 0, width * 0.15], [0, 1, height * 0.15]], dtype=float)
        tmp2 = cv2.warpAffine(img_zeros, M, (width, height))
        h2con = cv2.hconcat([dst[i]])

    if i == 3:
        for j, angle in enumerate(angles):
            rotation_matrix = cv2.getRotationMatrix2D((center_x, center_y), angle, scale)
            tmp1 = cv2.warpAffine(img, rotation_matrix, (0, 0))

            dst1.append(tmp1)

        h3con = cv2.hconcat([dst1[j - 1], dst1[j]])

result = cv2.vconcat([h1con, h2con])

cv2.imshow("result", h2con)
cv2.waitKey(0)
cv2.destroyAllWindows()