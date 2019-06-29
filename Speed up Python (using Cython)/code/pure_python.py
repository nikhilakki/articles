

def fibonacci_series(n: int):
    i = 0
    a = 1
    b = 1
    fib = []
    fib.append(a)
    fib.append(b)
    while i < n:
        c = a + b
        fib.append(c)
        a = b
        b = c
        i += 1
    return fib
