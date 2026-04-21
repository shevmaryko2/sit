def fib(n):
    if n <= 0:return
    a, b = 0, 1
    for i in range(n):
        print(a)
        a, b = b, a + b
fib(10) 