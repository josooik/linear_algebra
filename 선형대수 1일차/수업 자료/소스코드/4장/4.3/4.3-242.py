import cv2
import numpy as np


img = cv2.imread('image.jpg', cv2.IMREAD_COLOR)
height,width = img.shape[:2]


# 0.5배 축소하는 변환행렬을 생성합니다.
scale_factor = 0.5
scaling_matrix = np.array([[scale_factor, 0, 0], [0, scale_factor, 0], [0, 0, 1]])


dst = np.zeros((height, width, img.shape[2]) , dtype=np.uint8)

for y in range(height):
	for x in range(width):

		new_p = np.array([x, y, 1])
		inv_scaling_matrix = np.linalg.inv(scaling_matrix)
		old_p = np.dot(inv_scaling_matrix, new_p)

		x_,y_ = old_p[:2]
		x_ = int(x_)
		y_ = int(y_)

		# 입력 이미지의 좌표 (x,y)에 있는 픽셀의 Blue, Green, Red 채널을 결과 이미지에 저장합니다. 
		# 주어진 좌표의 픽셀값을 가져오는 itemset 메소드에서는 (x,y)대신에 (y,x)를 사용합니다. 
		if x_ > 0 and x_ < width and y_ > 0 and y_ < height:
			dst.itemset((y, x, 0), img.item(y_, x_, 0)) # blue 채널
			dst.itemset((y, x, 1), img.item(y_, x_, 1)) # green 채널
			dst.itemset((y, x, 2), img.item(y_, x_, 2)) # red 채널
			 
cv2.imshow("result", dst)
cv2.waitKey(0)
