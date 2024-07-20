import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
df=sns.load_dataset('diamonds')
df.head()
fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(df[:99].depth,df[:99].table,df[:99].price)
plt.show()
