def fib(n):
    if n == 0 or n == 1:
        return n
    n = fib(n-1) + fib(n-2)
    return n