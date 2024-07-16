import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('Soilders.csv')

plt.figure(figsize=(10, 6))
plt.bar(data['Soldiers'], data['Rating'])
plt.xlabel('Character')
plt.ylabel('Rating')
plt.title('Character Ratings Histogram')
plt.xticks(rotation=45)
plt.show()
