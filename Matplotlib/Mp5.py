import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

returns = pd.read_csv('Returns.csv')
plt.figure(figsize=(8,5))
plt.title('Returns Generated', fontdict={'fontweight':'bold', 'fontsize': 18})

plt.plot(returns.Year, returns['Charlie'], 'r.-')
plt.plot(returns.Year, returns['Peter'], 'g.-')

plt.xticks(returns.Year[::1].tolist()+[2011])
plt.xlabel('Year')
plt.ylabel('Returns')
plt.legend()
plt.savefig('Returns.png', dpi=300)
plt.show()
