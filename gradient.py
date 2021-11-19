import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 100, 255, dtype=int)
y = np.linspace(0, 100, 255, dtype=int)

arr_x, arr_y = np.meshgrid(x, y)
plotArray = arr_x + arr_y

color = "BuPu_r"

plt.imshow(plotArray, cmap=color)
plt.show()