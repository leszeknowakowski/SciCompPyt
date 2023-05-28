import numpy as np
import matplotlib.pyplot as plt


points = np.random.rand(100, 2)
x = points[:, 0]
y = points[:, 1]

dist = np.sqrt(x**2 + y**2)

col = []
for d in dist:
    if d < 1:
       col.append('green')
    else:
        col.append('red')

size = 50 * ( np.abs(x) + np.abs(y) ) #size increased 50 times for better visibility

plt.scatter(x, y, s=size, c = col)
plt.show()
