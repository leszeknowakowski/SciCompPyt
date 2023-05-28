import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,10,1000)

y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.exp(-x)

plt.plot(x,y1, "r", linestyle = "solid", label = "sin(x)")
plt.plot(x,y2, "g", linestyle = "dashed", label = "cos(x)")
plt.plot(x,y3, "b", linestyle = "dotted", label = "exp(-x)")
plt.legend()
plt.show()