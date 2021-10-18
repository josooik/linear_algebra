# 이미지 로드
import cv2

# 이미지 로드
img_src = cv2.imread('img/img1.jpg', cv2.IMREAD_COLOR)

# 이미지 사이즈 조정
img_size = cv2.resize(img_src, dsize=(800, 500), interpolation=cv2.INTER_AREA)

# 이미지 화면에 출력
cv2.imshow("result", img_size)

# 아무키나 입력할때 까지 대기
cv2.waitKey(0)

# 모든 창 닫기
cv2.destroyAllWindows()