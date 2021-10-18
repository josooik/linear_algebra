# 기저 벡터가 아닌 경우
import numpy as np
import matplotlib.pyplot as plt

# 벡터 공간 : 같은 개수의 성분을 가진 벡터로구성도니 집합 V가 있을 때 다음 두 조건을 만족하면 벡터 집합 V를 벡터 공간 이라고 합니다.
# 벡터 u,v,w는 벡터 집합 V의 원소이며 a, b는 임의의 스칼라 입니다.

# 부분 공간 : 벡터 공간의 부분 집합인 W가 당므 3가지 만족하면 부분 공간 이라고 합니다.
# 1.영벡터가 부분 공간의 원소, 0 (= W
# 2.벡터 v1과 v2가 부분 공간 W의 원소라면 v1 + v2도 부분 공간 W의 원소입니다.
# 3.c를 실수 스ㅏㄹ라라고 할 때 부분 공간 W의 원소 v1에 ㅇ미의의 스칼라 c를 곱한 cv1도 부분 공간 W의 원소가 됩니다. 즉, 스칼라곱에 대해 닫혀 있습니다.

a = np.array([2, 1])
b = np.array([-3, 2])
c = np.array([-6, 4])

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

ax.quiver(0, 0, a[0], a[1], angles='xy', scale_units='xy', scale=1, zorder=2)
ax.text(a[0], a[1], "a", size=15)

ax.quiver(0, 0, b[0], b[1], angles='xy', scale_units='xy', scale=1)
ax.text(b[0], b[1], "b", size=15)

ax.quiver(0, 0, c[0], c[1], angles='xy', scale_units='xy', scale=1, color='blue', zorder=1)
ax.text(c[0], c[1], "c", size=15, color='blue')

ax.set_xticks(range(-8, 4))
ax.set_yticks(range(-2, 6))

ax.grid()
ax.set_axisbelow(True)
ax.set_aspect('auto', adjustable='box')

ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

plt.show()