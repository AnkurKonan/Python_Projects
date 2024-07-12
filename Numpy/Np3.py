import numpy as np

a = np.array([1,2,3,4])
b = np.array([1,0,1,0])
print(a)
print(a + 2)
print(a - 2)
print(a * 2)
print(a / 2)
print(a + b)
print(a ** 2)
print(np.cos(a))
print(np.sin(a))

a = np.ones((2,3))
print(a)
b = np.full((3,2), 2)
print(b)
np.matmul(a,b)
c = np.identity(3)
np.linalg.det(c)
