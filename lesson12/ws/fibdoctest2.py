def fibonacci(n):

    old, new = 0, 1
    for _ in range(n):
        old, new = new, old + new
    return old

if __name__ == "__main__":
    import doctest
##    doctest.tesfile('test.txt')   no testfile object!