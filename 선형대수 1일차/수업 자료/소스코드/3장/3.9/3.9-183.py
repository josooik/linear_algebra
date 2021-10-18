import numpy as np
import matplotlib.pyplot as plt


A = np.array([[7, 2], [-7, 5]])
b = np.array([-5, 12])

x = np.linalg.solve(A, b)

# 해벡터인 x를 그래프로 표현하기 위해 x1, y1로 표기합니다.
x1, y1 = x
print(x1, y1)


fig = plt.figure() 
ax = fig.add_subplot(1, 1, 1)


# 선형 방정식을 직선으로 그립니다. 
a1 = A[:, 0]
b1 = A[:, 1]
c1 = -b

# c1x + c2y = c3
# c2y = c3 - c1x
# y = (c3-c1x)/c2

for c1, c2, c3 in zip(A[:, 0], A[:, 1], b):
    x = np.linspace(-7, 7, 100)
    y = (c3-c1*x)/c2
    ax.plot(x, y, color="black")


# 연립 방정식의 해를 빨간점으로 표시합니다.
ax.plot(x1, y1, 'ro')

ax.axis([-7, 7, -7, 7])
ax.set_xticks(range(-7, 7))
ax.set_yticks(range(-7,7))
ax.grid()
ax.set_axisbelow(True)
ax.set_aspect('equal', adjustable='box')

ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')

ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

plt.show()
