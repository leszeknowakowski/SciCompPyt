def iter_even():
    count = 0
    while True:
        yield count
        count += 2
print("iteration of even numbers:")
for i in iter_even():
    print(i)
    if i > 9:
        break

def iter_odd():
    count = 1
    while True:
        yield count
        count += 2
print("iteration of odd numbers:")
for i in iter_odd():
    print(i)
    if i > 10:
        break

def iter_power(k):
    i=0
    while True:
        yield k**i
        i+=1

print("iteration of powers: ")
for i in iter_power(10):
    print(i)
    if i > 10**6:
        break
