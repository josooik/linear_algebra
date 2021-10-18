import cv2
import numpy as np


# (x,y)에 있는 픽셀을 위해 보간법을 적용하는 함수입니다.
def BilinearInterpolation(Q11, Q12, Q21, Q22, x1, x2, y1, y2, x, y):

	P = 1/((x2-x1)*(y2-y1))*(Q11*(x2-x)*(y2-y)+Q21*(x-x1)*(y2-y)+Q12*(x2-x)*(y-y1)*Q22*(x-x1)*(y-y1))

	return P


img = cv2.imread('image.jpg', cv2.IMREAD_COLOR)
height,width = img.shape[:2]


# 0.5배 축소하는 변환행렬을 생성합니다. 
scale_factor = 0.5
new_width = int(width*scale_factor)
new_height = int(height*scale_factor)
scaling_matrix = np.array([[scale_factor, 0, 0], [0, scale_factor, 0], [0, 0, 1]])


# backward mapping을 사용하여 축소변환행렬 scaling_matrix을 이미지에 적용합니다. 
dst = np.zeros((new_height, new_width, img.shape[2]) , dtype=np.uint8)

for y in range(new_height):
	for x in range(new_width):

		new_p = np.array([x, y, 1])
		inv_scaling_matrix = np.linalg.inv(scaling_matrix)
		old_p = np.dot(inv_scaling_matrix, new_p)

		x_,y_ = old_p[:2]
		x_ = int(x_)
		y_ = int(y_)

		dst.itemset((y, x, 0), img.item(y_, x_, 0))
		dst.itemset((y, x, 1), img.item(y_, x_, 1))
		dst.itemset((y, x, 2), img.item(y_, x_, 2))


# 보간법을 적용합니다. 
dst2 = np.zeros((new_height, new_width, img.shape[2]) , dtype=np.uint8)

for y in range(new_height-1):
	for x in range(new_width-1):

		q11 = dst[y - 1, x - 1]
		q12 = dst[y + 1, x - 1]
		q21 = dst[y + 1, x + 1]
		q22 = dst[y - 1, x + 1]


		if dst[y, x].all() == 0:
			p = BilinearInterpolation(q11, q12, q21, q22, x - 1, x + 1, y - 1, y + 1, x, y);
	
		else:
			p = dst[y, x]

		dst2.itemset(y, x, 0, p[0])
		dst2.itemset(y, x, 1, p[1])
		dst2.itemset(y, x, 2, p[2])

			 
cv2.imshow("result", dst2)
cv2.waitKey(0)
