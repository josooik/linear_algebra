import numpy as np


A = np.array([[3, 2], [4, 1]])

print("A")
print(A)
print()


eigenvalue,eigenvector = np.linalg.eig(A)

print("고유값")
print(eigenvalue)
print("고유벡터")
print(eigenvector)
print()

# 고유벡터는 eigenvector의 열벡터입니다. 
eigenvector1 = eigenvector[:, 0]
eigenvector2 = eigenvector[:, 1]
eigenvalue1 = eigenvalue[0]
eigenvalue2 = eigenvalue[1]

# lambda * eigenvector와 A * eigenvector가 같음을 확인합니다. 
print("lambda * eigenvector == A * eigenvector")
print(eigenvalue1*eigenvector1, np.dot(A, eigenvector1))
print(eigenvalue2*eigenvector2, np.dot(A, eigenvector2))
