import math
list1 = list(range(0,16))

for i in list1:
    x = bin(list1[i])
    print(x)
    
for i in list1:
    y = hex(list1[i])
    print(y)
    
for i in list1:
    z= oct(list1[i])
    print(z)

#zaokrlaglanie
x = 5.876
print(round(x),int(x),math.trunc(x))

#range
print(list(range(1,2021,2)))
print(list(range(0,2022,2)))
print(list(range(0,2021,3)))