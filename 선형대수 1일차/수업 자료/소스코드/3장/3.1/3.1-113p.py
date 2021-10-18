import numpy as np
import matplotlib.pyplot as plt

# 3차원 그래프를 그리기 위해 추가해야 하는 모듈입니다. 
from mpl_toolkits.mplot3d import Axes3D


# 3차원 벡터 a
a = np.array([4, 5, 6])


fig = plt.figure() 

# 써브플롯에서 3차원 좌표계를 사용하도록 합니다. 
ax = fig.add_subplot(1, 1, 1, projection='3d')


# 시작점이 (0,0,0)이고 끝점 좌표가 변수 a의 값인  화살표를 그립니다. 
# a[0], a[1], a[2]가 각각 x, y, z 좌표입니다. 
ax.quiver(0, 0, 0, a[0], a[1], a[2], color='black', arrow_length_ratio=0.1)
ax.text( a[0], a[1], a[2], 'a', size=15)


# x, y, z 좌표축 범위가 각각 0~8인 그리드를 생성합니다. 
ax.set_xlim(0, 8)
ax.set_ylim(0, 8)
ax.set_zlim(0, 8)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.view_init(elev=20., azim=5)
ax.grid()
ax.set_axisbelow(True)
ax.set_aspect('equal', adjustable='box')

plt.show()
