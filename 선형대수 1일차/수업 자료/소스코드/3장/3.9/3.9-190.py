import numpy as np
import matplotlib.pyplot as plt


A = np.array([[5, 5], [5, 5]])
b = np.array([10, 20])

a1 = A[:, 0]
b1 = A[:, 1]
c1 = -b


fig = plt.figure() 
ax = fig.add_subplot(1, 1, 1)


# c1x + c2y = c3
# c2y = c3 - c1x
# y = (c3 - c1x)/c2

# c1x + c2y = c3
# c1x = c3 - c2y
# x = (c3-c2y)/c1

for c1, c2, c3 in zip(A[:, 0], A[:, 1], b):


    if c2 == 0:
        y = np.linspace(-20, 20, 100) 
        x = (c3-c2*y)/c1
        plt.plot(x, y, color="black")
    else:
        x = np.linspace(-20, 20, 100)
        y = (c3-c1*x)/c2
        plt.plot(x, y, color="black")


ax.axis([-7, 7, -7, 7])
ax.set_xticks(range(-7, 7))
ax.set_yticks(range(-7, 7))
ax.grid()
ax.set_axisbelow(True)
ax.set_aspect('equal', adjustable='box')

ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')

ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

plt.show()
