import itertools

iter_a = itertools.cycle([0,1])

for i in range(10):
    print(next(iter_a))

##have no idea how to make random iterator...


iter_c = itertools.cycle([0, 1, 0, -1])
for i in range(10):
    print(next(iter_c))