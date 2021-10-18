import numpy as np

A = np.array([1, 2, 3])
print(A)

print()

print(len(A))

print()

for i in range(len(A)):
    print(f'A[{i}] : {type(A[i])}')

print()

B = np.array([[1, 2, 3], [4, 5]])
print(B)

print(len(B[0]))

print(len(B[1]))

A = [1, 2 , 3]
B = [-1, -2, -3]
c =[]

for a, b, in zip(A, B):
    c.append(a + b)

print(c)

print()

A = np.array([1, 2, 3])
B = np.array([-1, -2, -3])
C = A + B

print(C)

print()

a = np.array([0.1, 0.2, 0.3])

print(a)

print(a.dtype)

print(type(a[0]))

b = [1, 2, 3]

x = np.array(b)

print(x)

print(x.dtype)

print(type(x[0]))

c = np.array([1, 2, 3], dtype=np.float64)
print(c)

print(c.dtype)

print(type(c[0]))

d = np.array([1.1, 2.2, 3.3, 4.9])

print(d.dtype)

e = d.astype(np.int32)

print(e)

print()

A = np.array([[1, 2, 3], [4, 5, 6]])
print(A)

print()

print(type(A))

print()

print(A.ndim)

print()

print(A.shape)

print()

print(A.size)

print()

print(A.dtype)

print()

print(A.itemsize)

print()

print(A.data)

print()

b = np.array([1, 2, 3, 4, 5, 6])

print(b.max())

print()

print(b.min())

print()

print(b.sum())

print()

print(b.mean())

print()

c = np.array([[1, 2], [3, 4]])

print(c)

print()

print(c.sum(axis=0))  #열 방햐으로 계산

print()

print(c.sum(axis=1))  #행 방향으로 계산

print()

A = np.array([1, 2, 3])

print(type(A[0]))

print()

print(A.ndim)

print()

print(A.shape)

print()

print(A)

print()

B = np.array([[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11]])

print(B)

print()

print(B.shape)

print()

C = np.arange(24).reshape(2, 3, 4)

print(C)

print()

print(C.shape)

print()

print(np.arange(10000).reshape(100, 100))

print()

import sys

np.set_printoptions(threshold=sys.maxsize)

print(np.arange(10000).reshape(100, 100))

print()

import timeit

# 파이썬 리스트
print("파이썬 배열 속도 : ", timeit.timeit('[ i ** 2 for i in A]', setup='A=range(100)'))

# Numpy 배열
print("Numpy 배열 속도 : ", timeit.timeit('B ** 2', setup='import numpy as np; B=np.arange(100)'))

print()

A = [1, 2, 3]
B = [3, 5, 2]
C =[]

for a, b in zip(A, B):
    C.append(a + b)

print(C)

A = np.array([1, 2, 3])
B = np.array([3, 5, 2])

print(A + B)

print()

a = np.array([1, 2, 3, 4])

print(a.shape)

print()

a = np.array([1, 2])

print(np.dot(a, a))

print()

a = np.array([1, 2, 3, 4])

print(a)

print()

a.shape=1,4

print(a)

print()

print(a.shape)

print()

a.shape=4,1

print(a)

print()

print(a.shape)

print()

A = np.zeros((2, 3))

print(A)

print()

print(A.dtype)

print()

B = np.ones((2, 3))

print(B)

print()

print(B.dtype)

print()

C = np.empty((5, 5)) # empty() 함수는 초기화되지 않도록 지정한 크기의 배열을 생성합니다.

print(C)

print()

print(C.dtype)

print()

C1 = np.zeros((5, 5))

print(C1)

print()

D = np.random.random((3, 3))

print(D)

print()

# 1 ~ 9 사이의 무작위 값을 생성하여 크기 2 X 2인 배열의 원소로 사용합니다.
E = np.random.randint(1, 10, (2, 2))

print(E)

print()

# 연속 원소 배열 생성 함수

# np.arange(시작값, 마지막값, 간격)
# np.arange(시작값, 마지막값)
# np.arange(마지막값)

A = np.arange(0, 50, 5)

print(A)

print()

B = np.arange(0.1, 3.5)

print(B)

print()

C = np.arange(10)

print(C)

print()

# linspace() 함수는 지정한 범위 내에 원하는 원소 개수로 숫자를 뽑아서 배열을 생성합니다.
# np.linspace(시작값, 마지막값, 샘플 개수)
# np.linspace(시작값, 마지막값)

A = np.linspace(0, 10, 10)

print(A)

print()

print(A.size)

print()

# 샘플 개수를 지정하지 않으면 디폴트 값은 50입니다.

B = np.linspace(0, 100)

print(B)

print()

print(B.size)

print()

# shape 변환 함수

A =np.arange(16)

B = A.reshape(4, 4)

print(B)

print()

print(B.shape)

print()

# 다른 배열의 데이터를 공유하고 있는 뷰라면 해당 배열이 출력됩니다.
print(A.base)

print()

print(B.base)

print()

print(B.base is A)

print()

B[0] = -1

print(A)

print()

print(B)

print()

# copy() 함수
C = B.reshape(2, 8).copy()

print(C)

print()

print(C.shape)

print()

C[0] = 0

print(B)

print()

print(C)

print()

C = np.arange(16)

print(C)

print()

# 변환될 배열의 열을 8로 지정하고 행은 -1로 지정하면 자동으로 행의 수가 계산 됩니다.
D = C.reshape(8, -1)

# 8 X 2 배열 생성
print(D)

print()

print(D.shape)

print()

E = C.reshape(-1, 8)

print(E)

print()

print(E.shape)

print()

# ravel 매소드는 배열을 1차원 배열로 변환하여 리턴합니다.
# 2 X 2 배열을 생성합니다.
A = np.array([[1, 2], [3, 4]])

print(A)

print()

print(A.shape)

print()

# ravel 메소드는 주어진 배열을 1차원 배열로 변환하여 리턴합니다.
B = A.ravel()

print(B)

print()

print(B.shape)

print()

print(B.base)  # 배열 B는 뷰이기 때문에 공유해준 배열이 출력됩니다.

print()

print(B.base is A)

print()

# resize 메소드는 뷰를 생성하지 않고, 배열의 shape를 직접 바꿉니다.
A = np.arange(12)

print(A)

print()

A.resize(3, 4)

print(A)

print()

# newaxis는 배열의 차원을 증가시켜줍니다. 1차원 배열을 열벡터 또는 행벡터로 바꿀때 사용할 수 있습니다.
a = np.array([1, 2, 3])

print(a)

print()

a = a[:, np.newaxis] # 열벡터 증가

print(a.shape)

print()

print(a)

print()

b = np.array([4, 5, 6])

print(b)

print()

b = b[np.newaxis, :] # 행벡터 증가

print(b.shape)

print()

print(b)