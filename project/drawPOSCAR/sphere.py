import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
r = 1

u, v = np.mgrid[0:2 * np.pi:50j, 0:np.pi:50j]
x = r * np.cos(u) * np.sin(v)
y = r * np.sin(u) * np.sin(v)
z = r * np.cos(v)

surf = ax.plot_surface(x, y, z, linewidth=0, antialiased=False)

plt.show()