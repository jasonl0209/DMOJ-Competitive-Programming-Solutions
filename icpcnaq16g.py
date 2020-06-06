from math import *
n = input()
length = len(n)
if length < 4:
    if length == 1:
        if n == "1":
            print(1)
        elif n == "2":
            print(2)
        else:
            print(3)
    elif length == 2:
        print(4)
    else:
        if n == "120":
            print(5)
        else: 
            print(6)
else:
    xi = 1
    log10_factorial = 0
    while log10_factorial < length:
        log10_factorial += log10(xi)
        if log10_factorial < length:
            xi += 1
    print(xi-1)