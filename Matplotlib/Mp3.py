import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = pd.read_csv('Soilders.csv')

left = data.loc[data['Division'] == 'Military police'].count()[0]
right = data.loc[data['Division'] == 'Survey corps'].count()[0]
plt.figure(figsize=(8,5))
labels = ['Military police', 'Survey corps']
colors = ['#fcc630', '#f23f3f']
plt.pie([left, right], labels = labels, colors=colors, autopct='%.2f %%')
plt.title('Foot Preference of FIFA Players')
plt.show()
