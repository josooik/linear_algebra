import cv2
import numpy as np

img = cv2.imread('img/img1.png', cv2.IMREAD_COLOR)

height, width = img.shape[:2]

KM = np.array([[1, 0, 150], [0, 1, 50]], dtype=float)

dt = cv2.warpAffine(img, KM, (width, height))

result = cv2.hconcat([img, dt])

cv2.imshow("result", result)
cv2.waitKey(0)