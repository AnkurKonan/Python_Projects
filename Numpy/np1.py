import numpy as np

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
