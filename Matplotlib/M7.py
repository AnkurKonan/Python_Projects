import matplotlib.pyplot as plt
import numpy as np

np.random.seed(19680801)
N = 150
r = 2 * np.random.rand(N)
theta = 2 * np.pi * np.random.rand(N)
area = 200 * r**2
colors = theta
figure = plt.figure(figsize=(8, 6))
ax = figure.add_subplot(111, projection='polar')
c = ax.scatter(theta, r, c=colors, s=area, cmap='hsv', alpha=0.75)
ax.set_thetamin(45)
ax.set_thetamax(135)
plt.show()
