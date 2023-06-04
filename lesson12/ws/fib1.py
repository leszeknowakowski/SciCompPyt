def fibonacci(n):
    old, new = 0, 1
    for _ in range(n):
        old, new = new, old + new
    return old

if __name__ == "__main__":

    results = [(0,0), (1, 1), (2, 1), (10, 54)]

    for a, b in results:
     assert fibonacci(a) == b

    print("tests passed")