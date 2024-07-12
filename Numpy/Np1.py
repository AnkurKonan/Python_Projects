import numpy as np

#Basic
a = np.array([1,2,3], dtype='int32')
print(a)
print(a.ndim)
print(a.dtype)
print(a.itemsize)
print(a.nbytes)
print(a.size)

b = np.array([[9.0,8.0,7.0],[6.0,5.0,4.0]])
print(b)
print(b.shape)

#Modification
a = np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
print(a)
print(a[1, 5])
print(a[0, :])
print(a[:, 2])
print(a[0, 1:-1:2])
a[1,5] = 20
a[:,2] = [1,2]
print(a)

b = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(b)
print(b[0,1,1])
print(b[0,1,1])
print(b)

