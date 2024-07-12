import numpy as np

a = np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
print(np.zeros((2,3)))
print(np.ones((4,2,2), dtype='int32'))
print(np.full((2,2), 99))
print(np.full_like(a, 4))
print(np.random.rand(4,2))
print(np.random.randint(-4,8, size=(3,3)))
print(np.identity(5))

arr = np.array([[1,2,3]])
r1 = np.repeat(arr,3, axis=0)
print(r1)
output = np.ones((5,5))
print(output)
z = np.zeros((3,3))
z[1,1] = 9
print(z)
output[1:-1,1:-1] = z
print(output)

a = np.array([1,2,3])
b = a.copy()
b[0] = 100
print(a)
