

cpdef list fibonacci_series(int n):
    cdef int i = 0
    cdef int a = 1
    cdef int b = 1
    cdef int c = 0
    cdef list fib = []
    fib.append(a)
    fib.append(b)

    while i < n:
        c = a + b
        fib.append(c)
        a = b
        b = c
        i += 1
    return fib
