# 벡터 뺼셈
import numpy as np
import matplotlib.pyplot as plt

a = np.array([4, 1])
b = np.array([-2, 3])

print(a - b)

print()

print(np.subtract(a, b))

print()

sub = a - b

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

# 원점에서 시작하도록 벡터 a를 그립니다.
ax.quiver(0, 0, a[0], a[1], angles='xy', scale_units='xy', scale=1)
ax.text(a[0], a[1], "a", size=15)

# 벡터 a의 끝점에서 시작하는 바대 방향의 벡터 b를 그립니다.
ax.quiver(a[0], a[1], -b[0], -b[1], angles='xy', scale_units='xy', scale=1)
ax.text(a[0] - b[0], a[1] - b[1], "-b", size=15)

# 두 벡터의 뺄셈 결과를 그려보면 벡터 a의 시작점과 벡터 b의 끝점을 잇는 선입니다.
ax.quiver(0, 0, sub[0], sub[1], angles='xy', scale_units='xy', scale=1, color='red')
ax.text(sub[0] * 0.5 + 0.3, sub[1] * 0.5, "a - b", size=15, color='red')

ax.set_xticks(range(-2, 8))
ax.set_yticks(range(-4, 5))
ax.grid()
ax.set_axisbelow(True)
ax.set_aspect('equal', adjustable='box')

ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

plt.show()