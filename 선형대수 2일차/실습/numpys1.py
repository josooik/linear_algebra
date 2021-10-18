import numpy as np

A = np.array([[1, 2], [3, 4]])
B = np.array([[1, 0], [0, 1]])

print(A)

print()

print(B)

print()

# Vstack() 열방향 결합
C = np.vstack((A, B))

print(C)

print()

# hstack () 행방향 결합
D = np.hstack((A, B))

print(D)

print()

# column_stack() 1차원 배열을 열벡터로 하는 2차원 배열을 만듭니다.
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
c = np.array([7, 8, 9])

E = np.column_stack((a, b, c))

print(E)

print()

# np.row_stack() 행방향 결합
E1 = np.row_stack((a, b))

print(E1)

print()

# concatenate() 지정한 차원 방향으로 배열을 결합합니다.
A = np.array([[1, 2], [3, 4]])
B = np.array([[1, 0], [0, 1]])

print(A)

print()

print(B)

print()

print(np.concatenate((A, B), axis=0)) # 열방향

print()

print(np.concatenate((A, B), axis=1)) # 행방향

print()

# 배열 분할 함수
# 배열을 2개이상의 배열로 나눌때 사용
# 행방향 분할(가로방향) : hsplit
# hsplit(분할할 행렬, 분할 개수)
# hsplit(분할 행렬, (기준점1, 기준점2, ...)

A = np.arange(9).reshape(3, 3)

print(A)

print()

a = np.hsplit(A, 3) # 배열을 행 방향으로 3개로 분할합니다.

print(a)

print()

print(a[0])

print()

print(a[1])

print()

print(a[2])

print()

B = np.arange(18).reshape(3, 6)

print(B)

print()

# 지정한 범위를 기준으로 다음과 같이 3개로 분할합니다.
# B[:, 0:2], B[:, 2:5], B[:, 5:]
b = np.hsplit(B, (2, 5))

print(b)

print()

print(b[0])

print()

print(b[1])

print()

print(b[2])

print()

# 열방향 분할(세로방향) : vsplit
A = np.arange(9).reshape(3, 3)

print(A)

print()

a = np.vsplit(A, 3)

print(a)

print()

print(a[0])

print()

print(a[1])

print()

print(a[2])

print()

B = np.arange(24).reshape(6, 4)

print(B)

print()

# B[:1, :], B[1:4, :], B[4:, :]

b = np.vsplit(B, (1, 4))

print(b)

print()

print(b[0])

print()

print(b[1])

print()

print(b[2])

print()

# 인덱싱

A = np.arange(0, 15, 2)

print(A)

print()

print(A.shape)

# 인덱스가 -1이면 역순으로 출력
print(A[-1])

print()

print(A[-2])

print()

print(A[-3])

print()

A = np.arange(12).reshape(3, 4)

print(A)

print()

print(A.ndim)

print()

print(A[2, 2])

print()

A = np.arange(12).reshape(3, 4)

height, width = A.shape
for i in range(height):
    for j in range(width):
        print("A[%d %d] : %d" %(i, j, A[i,j]))

print()

A = np.arange(9).reshape(3, 3)

print(A)

print()

for row in A:
    print(row)

print()

# 열벡터 출력
# A.T는 A의 행과 열을 교환하여 얻게되는 전치행렬입니다.
for column in A.T:
    print(column)

print()

# flat을 사용하면 배열의 원소를 개별 출력
A = np.arange(9).reshape(3, 3)
for a in A.flat:
    print(a)

print()

# 슬라이싱

A = np.arange(0, 15, 2) # 1차원 배열

print(A)

print()

print(A[0:3])

print()

print(A)

print()

print(A[0:4])

print()

print(A[:4])

print()

print(A[6:8])

print()

print(A[6:])

print()

print(A[:])

print()

print(A[::2])

print()

print(A[: -2])

print()

print(A[-2:])

print()

print(A[0:3].shape)

print()

print(A[0:3].ndim)

print()

print(A)

print()

A[0:3] = 100

print(A)

print()

A = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(A)

print()

print(A.shape)

print()

print(A[1, 2])

print()

print(A[1][2])

print()

print(A[0])

print()

print(A[1])

print()

print(A[:, 0])

print()

print(A[:, 1])

print()

print(A)

print()

print(A[:2, :2])

print()

A[:2, :2] = 0
print(A)

print()

print(A[:2, :2])

print()

A = np.arange(12).reshape(3, 4)

print(A)

print()

print(A[0])

print()

print(A[1])

print()

# 하나 이상의 인덱스를 생략시 ...를 사용할 수 있습니다.
print(A[..., 0])

print()

print(A[..., 1])

print()

# 대입
a = np.arange(12)
b = a

print(b)

print()

print(a == b)

print()

print(a is b)

print()

a[0] = 100
b[11] = -1

print(a)

print()

print(b)

print()

b.shape=3, 4

print(b)

print()

print(a.shape)

print()

# 함수로 전달될 떄에도 같은 넘파이 객체에 접근합니다.
# 함수 아규먼트의 id와 함수 파라미터의 id값이 동일합니다.
def f(x):
    print(id(x))

a = np.array([1, 2])
print(id(a))

print()

print(f(a))

print()

# 얕은 복사 : 기존 배열의 원소를 공유하는 새로운 배열을 생성합니다.
# 얕은 복사 : view() 사용
a = np.arange(12)

b = a.view()

print(a)

print()

print(b)

print()

print(b.base is a)

print()

print(a is b)

print()

a[0] = -1
b[11] = 100

print(a)

print()

print(b)

print()

a.resize(3, 4)
print(a)

print()

print(b)

print()

a[0, 2] = 10000

print(a)

print()

print(b)

print()

c = a[0]
c[:] = 0
print(c)

print()

print(a)

print()

print(b)

print()

# 깊은 복사 : 기존 배열의 데이터를 공유하지 안는 복사본이 필요한 경우 copy 메소드를 사용할 수 있습니다.
# 깊은 복사 : copy() 사용
a = np.arange(12)

# np.copy() 메소드를 사용하면 새로운 Numpy 객체의 새로운 메모리 공간에 배열 a의 데이터를 복사합니다.
b = a.copy()

print(a)

print()

print(b)

print()

print(a == b)

print()

print(a is b)

print()

print(b.base is a)

print()

a[0] = -1
b[11]= 100

print(a)

print()

print(b)

print()

# 산술 연산과 브로드캐스팅
# 같은 크기의 배열 간의 연산
a = np.array([2, 4, 6, 8]).reshape(2, 2)
b = np.array([2, 2, 2, 2]).reshape(2, 2)

print(a)

print()

print(b)

print()

print(a + b)

print()

print(a - b)

print()

# 행렬 곱셈
print(a * b)

print()

# 행렬 곱셈
print(np.dot(a, b))

print()

# 행렬 곱셈
print(a @ b)

print()

print(a / b)

print()

# 다른 크기의 배열간의 연산
# 브로드캐스팅 : 대응하는 차원 크기가 같거나 한쪽이 1인경우 브로드캐스팅이 가능합니다.

A = np.arange(10, 130, 10).reshape(3, 4)
print(A)

print()

B = np.arange(1, 5)
print(B)

print()

print(A + B)

print()

A = np.arange(10, 130, 10).reshape(3, 4)
print(A)

print()

B = 5
print(B)

print()

print(A + B)
