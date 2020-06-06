import sys
modulo = 1000000007
dict_fibo = {1:1, 2:1}
def fibonacci(n):
    if n in dict_fibo: return dict_fibo.get(n)
    if n % 2 == 0:
        dict_fibo[n] = fibonacci(n//2) * (2 * fibonacci((n//2) + 1) - fibonacci(n//2)) % modulo
        return dict_fibo.get(n)
    else:
        dict_fibo[n] = (fibonacci(((n-1)//2) + 1) * fibonacci(((n-1)//2) + 1) + fibonacci((n-1)//2) * fibonacci((n-1)//2)) % modulo
        return dict_fibo.get(n)
num = int(sys.stdin.readline())
fib1 = fibonacci(num)
fib2 = fibonacci(num+1)
out = fib1 + fib2 - 1
print(out%modulo)