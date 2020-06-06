n = int(input())
if n == 1:
    print(9)
elif n < 18:
    if n%2 == 0:
        total = n//2 * "1"
        print((18*int(total))%1000000000)
    else:
        total = n//2 * "1"
        print((18*int(total)+9*(10**(n//2)))%1000000000)
else:
    print(999999998)