#import sys for I/O
import sys
#answers output mod 10**9 + 7, a prime number
modulo = 1000000007
#Dictionary to store elements of fibonacci sequence
dict_fibo = {1:1, 2:1}
#Doubling Method - Based on Matrix Exponentiation
#https://funloop.org/post/2017-04-14-computing-fibonacci-numbers.html
#A recursive approach - approximately O(log(n) time complexity
def fibonacci(n):
    if n in dict_fibo: 
        return dict_fibo.get(n)
    if n % 2 == 0:
        dict_fibo[n] = fibonacci(n//2) * (2 * fibonacci((n//2) + 1) - fibonacci(n//2)) % modulo
        return dict_fibo.get(n)
    else:
        dict_fibo[n] = (fibonacci(((n-1)//2) + 1) * fibonacci(((n-1)//2) + 1) + fibonacci((n-1)//2) * fibonacci((n-1)//2)) % modulo
        return dict_fibo.get(n)
#2000000016 is the Pisano Period for 10**9+7
#Using stdin; faster than input()
num = int(sys.stdin.readline()) % 2000000016
out = fibonacci(num) % modulo
#Using stdout 
sys.stdout.write(str(out))