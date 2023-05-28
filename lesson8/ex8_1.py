import numpy as np

a = np.arange(0.0,1.0,0.1)
b = np.zeros((5,6),dtype="int8")
x = complex(0,1)
c = np.full(9,x) ** np.arange(0,9,1)
print(a.dtype)
print(b.dtype)
print(b.itemsize)
print(c)