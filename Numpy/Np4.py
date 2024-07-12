import numpy as np

# Statistics
stats = np.array([[1,2,3],[4,5,6]])
print(stats)
print(np.min(stats))
print(np.max(stats, axis=1))
print(np.sum(stats, axis=0))

# Miscellaneous
v1 = np.array([1,2,3,4])
v2 = np.array([5,6,7,8])
print(np.vstack([v1,v2,v1,v2]))
h1 = np.ones((2,4))
h2 = np.zeros((2,2))
print(np.hstack((h1,h2)))


