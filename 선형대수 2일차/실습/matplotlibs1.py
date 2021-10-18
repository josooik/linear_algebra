# 화살표 그리기
import numpy as np
import matplotlib.pyplot as plt

# 벡터 a를 정의합니다.
a = np.array([4, 3])

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

# 시작 위치는 (0, 0)이고 화살표가 그려지는 끝 위치는 변수 a의 값을 좌표로 사용하는 화살표를 그립니다.
# a[0]과 a[1]이 각각 끝 위치의 x좌표, y좌표입니다.
ax.quiver(0, 0, a[0], a[1], angles='xy', scale_units='xy', scale=1)
ax.text(a[0], a[1], 'a', size=15)

# x축, y축 눈금 범위를 0에서 6으로 지정합니다.
ax.set_xticks(range(0, 7))
ax.set_yticks(range(0, 7))
ax.grid()
ax.set_axisbelow(True)
ax.set_aspect('equal', adjustable='box')

ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

plt.show()