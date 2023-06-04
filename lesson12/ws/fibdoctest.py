def fibonacci(n):
    """
    calculates the nth Fibonacci number iteratively.

    >>> fibonacci(0)
    0
    >>> fibonacci(1)
    1
    >>> fibonacci(10)
    55
    >>> fibonacci(15)
    610
    >>>

    """
    old, new = 0, 1
    for _ in range(n):
        old, new = new, old + new
    return old

if __name__ == "__main__":
    import doctest
    doctest.testmod()