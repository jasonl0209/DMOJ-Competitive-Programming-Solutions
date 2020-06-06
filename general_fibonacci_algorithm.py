from sys import *
a, b, n = map(int, stdin.readline().split())
if n == 0: 
    print(a)
elif n == 1: 
    print(b)
else:
    modulo = 1000000000
    dict_fibo = {1:1, 2:1}
    def fibonacci(n):
        if n in dict_fibo: 
            return dict_fibo.get(n)
        if n % 2 == 0:
            dict_fibo[n] = (fibonacci(n//2) * (2 * fibonacci((n//2) + 1) - fibonacci(n//2))) % modulo
            return dict_fibo.get(n)
        else:
            dict_fibo[n] = (fibonacci(((n-1)//2) + 1) ** 2 + fibonacci((n-1)//2) ** 2) % modulo
            return dict_fibo.get(n)
    t1 = fibonacci(n-1) * a 
    t2 = fibonacci(n) * b
    out = (t1 + t2) % modulo
    print(out)