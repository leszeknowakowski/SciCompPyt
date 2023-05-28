def reverse_range1(L,left,right):
    while left < right:
        #L[left],L[right] = L[right],L[left]
        x = L[left]
        L[left] = L[right]
        L[right] = x
        left +=1
        right-=1

def iter_count(start=0, step=1):
    i = start
    while True:
        yield i
        i = i + step

def iter_power(k): #faster, only one more multiplication in each loop
    i = 1
    while True:
        yield i
        i = i * k

even, odd, iter = iter_even(), iter_odd(), iter_power(2)
for i in range(7):
    print( "{:3d} {:3d} {:3d}".format(next(even), next(odd), next(power)))

