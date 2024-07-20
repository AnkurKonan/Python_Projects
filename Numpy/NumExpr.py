# Comparision of numpy & numpexpr (time taken to complete the process) 
import time
import numpy as np
import numexpr as ne
a = np.random.rand(100000000)
b = np.random.rand(100000000)
start = time.time()
result = a * b * np.sin(a)
end = time.time()
print('Numpy Time:', end - start)
start = time.time()
result_ne = ne.evaluate('a * b * sin(a)')
end = time.time()
print('NumExp Time:', end - start)

