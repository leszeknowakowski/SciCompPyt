import numpy as np
import matplotlib.pyplot as plt

Nx, Nt, L, T, c = 20, 100, 1.0, 2.0, 1.0

t = np.linspace(0, T, num=Nt+1, dtype=float)
x = np.linspace(0, L, num=Nx+1, dtype=float)

dx = x[1] - x[0]
dt = t[1] - t[0]

r = (c*dt/dx)**2
print("r = {}".format(r))
assert r < 1.0

u = np.empty( (Nx+1, Nt+1), dtype=float)
##initial condition t = 0
u[:,0] = np.sin(x * np.pi*(3))

##boundary conditions, x = 0 and x = 1
u[0,:] = 0.0
u[Nx,:] = 0.0


assert abs(u[0,0]< 1e-6) and abs(u[Nx,0] < 1e-6)

# initial condition j=1
u[1:-1,1] = u[1:-1,0] + (r*0.5)*( u[:-2,0] -2*u[1:-1,0] + u[2:,0] )

# iteration/solution the linear algebraic equations
for j in range(1,Nt):
    u[1:-1,j+1] = -u[1:-1,j-1] +2*u[1:-1,j] + r*(u[:-2,j] -2*u[1:-1,j] + u[2:,j])



plt.title("one dimensional wave propagation")
plt.xlabel("time")
plt.ylabel("x")
for slice in range(len(t))[::14]:
    plt.plot(x, u[:, slice], label = "time {}".format(slice))
#plt.imshow(u, cmap='viridis', interpolation='hamming')
#plt.colorbar()
plt.legend()
plt.show()