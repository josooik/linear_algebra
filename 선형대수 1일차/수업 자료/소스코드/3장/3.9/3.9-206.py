import numpy as np
import matplotlib.pyplot as plt


A = np.array([[0, 1], [-2, 1], [2, 1]])
b = np.array([-1, -4, 8])
x = np.linalg.lstsq(A, b, rcond=-1)[0]


# 해벡터인 x를 그래프로 표현하기 위해 x1, y1로 표기합니다.
x1, y1 = x


a1 = A[:, 0]
b1 = A[:, 1]
c1 = -b



fig = plt.figure() 
ax = fig.add_subplot(1, 1, 1)


# c1x + c2y = c3
# c2y = c3 - c1x
# y = (c3 - c1x)/c2

for c1, c2, c3 in zip(A[:, 0], A[:, 1], b):

    x = np.linspace(-20, 20, 100)
    y = (c3-c1*x)/c2
    ax.plot(x, y, color="black")


ax.plot(x1, y1, 'ro')



ax.axis([-2, 6, -2, 6])
ax.set_xticks(range(-2, 6))
ax.set_yticks(range(-2, 6))
ax.grid()
ax.set_axisbelow(True)
ax.set_aspect('equal', adjustable='box')

ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')

ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

plt.show()
