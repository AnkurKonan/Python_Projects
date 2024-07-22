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


# Comparision of numpy & numpexpr by taking another expression (time taken to complete the process) 
import time
import numpy as np
import numexpr as ne
import pandas as pd
df = pd.DataFrame({
    'A': np.random.rand(20000000),
    'B': np.random.rand(20000000),
    'C': np.random.rand(20000000),
    'D': np.random.rand(20000000)
})
start_pd = time.time()
df['G'] = (df['A'] ** 2 + df['B'] ** 2) ** 0.5
end_pd = time.time()
start_ne = time.time()
A, B, C, D = df['A'].values, df['B'].values, df['C'].values, df['D'].values
G = ne.evaluate('(A ** 2 + B ** 2) ** 0.5')
end_ne = time.time()
print("Pandas time: ", end_pd - start_pd)
print("NumpExpr time: ", end_ne - start_ne)
