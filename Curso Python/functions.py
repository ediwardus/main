def fib(n):    # write Fibonacci series less than n
    """Print a Fibonacci series less than n."""
    a, b = 0, 1
    result = []
    while a < n:
        result.append(a)
        print(a, end=' ')
        a, b = b, a+b
    return result