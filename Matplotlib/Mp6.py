import pandas as pd
import matplotlib.pyplot as plt

corps = pd.read_csv('Soldiers.csv')
corps['Rating'] = corps['Rating'].astype(int)
Badass = corps[corps['Rating'] == 10].count()[0]
Strong = corps[(corps['Rating'] >= 7) & (corps['Rating'] <= 9)].count()[0]
Decent = corps[(corps['Rating'] >= 5) & (corps['Rating'] <= 6)].count()[0]
Average = corps[corps['Rating'] < 5].count()[0]

weights = [Average, Decent, Strong, Badass]
labels = ['Average', 'Decent', 'Strong', 'Badass']
explode = (0.1, 0.1, 0, 0.1)

plt.figure(figsize=(8, 5), dpi=100)
plt.title('Skills Rating of Soldiers')
plt.pie(weights, labels=labels, explode=explode, autopct='%.2f %%', startangle=140)
plt.show()
