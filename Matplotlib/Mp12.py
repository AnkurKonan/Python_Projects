#Animation
import numpy as np
import random
import matplotlib.pyplot as plt
from matplotlib import style

one_two = [0,0]
for _ in range(100000):
    one_two[random.randint(0,1)] += 1
    plt.bar(["heads", "tail"], one_two, color=["red", "blue"])
    plt.pause(0.001)
plt.show()

#Animation_2
import numpy as np
import random
import matplotlib.pyplot as plt
from matplotlib import style

counts = [0, 0, 0, 0, 0]
labels = ["Goku", "Vegeta", "Gohan", "Trunks", "Picolo"]
colors = ["#fc4903", "#010e80", "#fc4903", "#aeaeb0", "#55bd00"]
style.use('ggplot')
fig, ax = plt.subplots()
for _ in range(100000):
    counts[random.randint(0, 4)] += 1
    ax.clear()
    ax.bar(labels, counts, color=colors)
    plt.pause(0.001)
plt.show()
