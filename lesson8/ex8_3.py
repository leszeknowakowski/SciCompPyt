import numpy as np

a = np.random.randint(1,15,size=20)
m1 = a.reshape(4,5)

m2 = np.flip(m1, axis=-1)
m3 = np.flip(m1, axis = 0)
m4 = m1[1:3,1:4]

print(m1)
print(m2)
print(m3)
print(m4)