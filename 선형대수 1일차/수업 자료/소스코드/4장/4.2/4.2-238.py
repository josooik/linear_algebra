import cv2
import numpy as np


img = cv2.imread('image.jpg', cv2.IMREAD_COLOR)
height,width = img.shape[:2]

# 45도를 라디안으로 변환하여 코싸인값과 싸인값을 구합니다.
angle = 45
radian = angle*np.pi/180
c = np.cos(radian)
s = np.sin(radian)

# 이미지 중심 좌표를 구합니다. 
center_x = width/2
center_y = height/2

# 회전변환행렬을 구성합니다.
rotation_matrix = np.array([[c, s, (1-c)*center_x-s*center_y], [-s, c, s*center_x+(1-c)*center_y], [0, 0, 1]])


dst = np.zeros(img.shape, dtype=np.uint8)

for y in range(height-1):
	for x in range(width-1):

		# backward mapping
		# 결과 이미지의 픽셀 new_p로 이동하는 입력 이미지의 
		# 픽셀 old_p의 위치를 계산합니다.
		new_p = np.array([x, y, 1])
		inv_rotation_matrix = np.linalg.inv(rotation_matrix)
		old_p = np.dot(inv_rotation_matrix, new_p)

		# new_p 위치에 계산하여 얻은 old_p 픽셀의 값을 대입합니다.
		x_,y_ = old_p[:2]
		x_ = int(x_)
		y_ = int(y_)

		if x_ > 0 and x_ < width and y_ > 0 and y_ < height:
			dst[y, x] = img[y_, x_]

			
result = cv2.hconcat([img, dst]) 
cv2.imshow("result", result)
cv2.waitKey(0)
