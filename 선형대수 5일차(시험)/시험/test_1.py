import numpy as np
import matplotlib.pyplot as plt

K = np.array([[5, 2], [-5, 3]])
B = np.array([9, 1])

x = np.linalg.solve(K, B)

# 해벡터인 x를 그래프로 표현하기 위해 x1, y1로 표기합니다.
x1, y1 = x
print(x1, y1)

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

# 선형 방정식을 직선으로 그립니다.
a1 = K[:, 0]
b1 = K[:, 1]
c1 = -B

for c1, c2, c3 in zip(K[:, 0], K[:, 1], B):
    x = np.linspace(-5, 5, 100)
    y = (c3 - c1 * x) / c2
    ax.plot(x, y, color="blue")

ax.plot(x1, y1, 'go')

ax.axis([-5, 5, -5, 5])
ax.set_xticks(range(-5, 5))
ax.set_yticks(range(-5, 5))
ax.grid()
ax.set_axisbelow(True)
ax.set_aspect('equal', adjustable='box')

ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')

ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

plt.show()