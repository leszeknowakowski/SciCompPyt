import numpy as np
import matplotlib.pyplot as plt

D, Nx, Nt, L, T = 1.0, 50, 1000 ,1.0 ,0.1

t = np.linspace(0, T, num=Nt+1, dtype=float)
x = np.linspace(0, L, num=Nx+1, dtype=float)

dx = x[1] - x[0]
dt = t[1] - t[0]

r = D*dt/(dx*dx)
print("r = {}".format(r))
assert r < 0.5

u = np.empty( (Nx+1, Nt+1), dtype=float)
##initial condition t = 0
u[:,0] = np.where(x < 0.5, np.where(x<0.75,0.5, 1), 0)

##boundary conditions, x = 0 and x = 1
u[0,:] = 1
u[Nx,:] = 0

for j in range(Nt):
    u[1:-1,j+1] = r*u[:-2,j] + (1-2*r)*u[1:-1,j] + r*u[2:,j]

plt.title("one dimensional heat propagation in bar")
plt.xlabel("time")
plt.ylabel("x")
plt.imshow(u, cmap='viridis', interpolation='nearest')
#plt.imshow(u[:,::5], cmap="viridis", )
plt.colorbar()
plt.show()