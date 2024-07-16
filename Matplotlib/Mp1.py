import matplotlib.pyplot as plt
import numpy as np

x = [0,1,2,3,4,5,6,7,8,9,10]
y = [0,1,2,3,4,5,6,7,8,9,10]
x2 = np.arange(0,4.5,0.5)

# Size of graph & dpi (pixels per inch)
plt.figure(figsize=(8,5), dpi=100)

# Simple line
plt.plot(x,y, label='2x', color='red', linewidth=2, marker='.', linestyle='-', markersize=10, markeredgecolor='blue')

# Ploting graph
plt.plot(x2[:6], x2[:6]**2, 'r', label='X^2')
plt.plot(x2[5:], x2[5:]**2, 'r--')
plt.title('The Graph', fontdict={'fontname': 'Apple Braille Outline 8 Dot', 'fontsize': 15})


