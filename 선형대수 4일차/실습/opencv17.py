# 호모그래피 행렬 구하기1
import cv2
import numpy as np

# 클릭한 횟수를 저장합니다.
count_mouse_click = 0

# 호모그래피 행렬을 곱해서 결과를 계산중이면 1을 갖게됩니다.
# 계산중에 마우스 클릭은 무시하기 위해서 사용됩니다. 
caculate_start = 0

# 마우스 클릭한 위치를 저장할 리스트입니다. 
pointX = []
pointY = []


# OpenCV 창에 보이는 이미지를 클릭시, 클릭한 위치(x,y)를 파라미터로 호출되는 콜백함수입니다.   
def CallBackFunc(event, x, y, flags, userdata):
    global count_mouse_click, caculate_start

    # 마우스 왼쪽 버튼을 클릭했는지 체크합니다.
    if event == cv2.EVENT_LBUTTONDOWN:
        print("{} - ({}, {} )".format(count_mouse_click, x, y))

        # 마우스 클릭한 위치를 저장합니다.
        pointX.append(x)
        pointY.append(y)

        # 마우스 클릭한 횟수를 업데이트합니다.
        count_mouse_click += 1

        # 마우스 클릭한 위치를 화면에 보여줄 때 사용하기 위해 입력 이미지를 복사합니다.  
        img_temp = img_gray.copy()

        # 마우스 클릭한 위치에 원을 그립니다. 
        for point in zip(pointX, pointY):
            cv2.circle(img_temp, point, 5, (0), 2 )

        # 마우스 클릭할때마다 원이 이미지에 보이게 됩니다.  
        cv2.imshow("gray image", img_temp)


    # 4점을 모두 클릭한 상태이고 아직 결과 이미지를 처리하기 전이면 
    if count_mouse_click == 4 and caculate_start == 0:
    
        # 이제 결과 이미지 처리중임을 알립니다. 
        caculate_start = 1;

        print("calculate H")

        # 클릭한 사각 영역좌표를 기반으로 정면에서 바라본 직사각형 영역을 계산합니다. 
        width = ((pointX[1] - pointX[0]) + (pointX[3] - pointX[2]))*0.5;
        height = ((pointY[2] - pointY[0]) + (pointY[3] - pointY[1]))*0.5;

        newpointX = np.array([pointX[3] - width, pointX[3], pointX[3] - width, pointX[3]])
        newpointY = np.array([pointY[3] - height, pointY[3] - height, pointY[3], pointY[3]])

        # 계산한 직사각형 영역을 화면에 출력합니다. 
        for i in range(4):
            print("({}, {})".format(newpointX[i], newpointY[i]))


        # 마우스로 클릭한 좌표와 계산된 좌표를 넘파이 배열로 변환합니다. 
        pts_src = []
        pts_dst = []

        for i in range(4):
            pts_src.append((pointX[i], pointY[i]))
            pts_dst.append((newpointX[i], newpointY[i]))

        pts_src = np.array(pts_src)
        pts_dst = np.array(pts_dst)


        # 호모그래피 행렬을 구합니다. 
        A = np.array([
            [ -1 * pointX[0], -1 * pointY[0], -1, 0, 0, 0,     pointX[0] * newpointX[0], pointY[0] * newpointX[0], newpointX[0] ],
            [ 0, 0, 0, -1 * pointX[0], -1 * pointY[0], -1,   pointX[0] * newpointY[0], pointY[0] * newpointY[0], newpointY[0] ],
            [ -1 * pointX[1], -1 * pointY[1], -1, 0, 0, 0,pointX[1] * newpointX[1], pointY[1] * newpointX[1], newpointX[1] ],
            [ 0, 0, 0, -1 * pointX[1], -1 * pointY[1], -1,pointX[1] * newpointY[1], pointY[1] * newpointY[1], newpointY[1] ],
            [ -1 * pointX[2], -1 * pointY[2], -1, 0, 0, 0,pointX[2] * newpointX[2], pointY[2] * newpointX[2], newpointX[2] ],
            [ 0, 0, 0, -1 * pointX[2], -1 * pointY[2], -1,pointX[2] * newpointY[2], pointY[2] * newpointY[2], newpointY[2] ],
            [ -1 * pointX[3], -1 * pointY[3], -1, 0, 0, 0,pointX[3] * newpointX[3], pointY[3] * newpointX[3], newpointX[3] ],
            [ 0, 0, 0, -1 * pointX[3], -1 * pointY[3], -1,pointX[3] * newpointY[3], pointY[3] * newpointY[3], newpointY[3] ]])


        u, s, v = np.linalg.svd(A, full_matrices=True)
        v = v.T

        # v의 마지막 컬럼값을 H로 취합니다. 
        temp = v[:,8]
        h = temp.reshape(3,3)

        # h_33을 1로 만듭니다. 
        h = h / h[2,2]


        img_result = np.zeros(img_gray.shape, dtype=np.uint8)

        height, width = img_gray.shape[:2]
        for y in range(height):
            for x in range(width):

                oldpoint = np.array([x, y, 1])
                newpoint = np.dot(h, oldpoint)

                newX = int(newpoint[0]/newpoint[2])
                newY = int(newpoint[1]/newpoint[2])

                if newX > 0 and newY > 0 and newX < width and newY < height:
                    img_result.itemset(newY, newX, img_gray.item(y, x))

        result = cv2.hconcat([img_gray, img_result]) 
        cv2.imshow("result", result)
        cv2.waitKey(0)

# 호모그래피 행렬을 저장할 입력 이미지를 로드합니다. 
img_gray = cv2.imread("img/img5.jpg", cv2.IMREAD_GRAYSCALE)

# 이미지 사이즈 조정
img_gray = cv2.resize(img_gray, dsize=(600, 600), interpolation=cv2.INTER_AREA)

# 타이틀바에 “gray image”를 출력하는 창에 넘파이 배열 img_gray를 보여줍니다. 
cv2.imshow("gray image", img_gray)

# 타이틀바에 “gray image”를 출력하는 창을 위해 마우스 콜백 함수를 지정합니다. 
cv2.setMouseCallback("gray image", CallBackFunc)

print("left up, right up, left down, right down")

cv2.waitKey(0)
