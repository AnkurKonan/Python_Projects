#Multiple figure
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
x1, y1 = np.random.random(100), np.random.random(100)
x2, y2 = np.arange(100), np.random.random(100)
plt.figure(1)
plt.scatter(x1, y1)
plt.figure(2)
plt.plot(x2, y2)
plt.show()

#Sub-plot figure
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
x = np.arange(100)
fig, axs = plt.subplots(2,3)
axs[0,0].plot(x, np.sin(x))
axs[0,0].set_title("Sin wave")
axs[0,1].plot(x, np.cos(x))
axs[0,1].set_title("cos wave")
axs[1,0].plot(x, np.random.random(100))
axs[1,0].set_title("Random function")
axs[1,1].plot(x, np.log(x))
axs[1,1].set_title("log function")
axs[0,2].plot(x, np.tan(x))
axs[0,2].set_title("tan wave")
axs[1,2].plot(x, np.square(x))
axs[1,2].set_title("square wave")
plt.show()
