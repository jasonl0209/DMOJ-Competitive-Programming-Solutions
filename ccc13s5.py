from sys import *
from math import *
num = int(stdin.readline())
counter = 0
while num > 1:
    bln_get = False
    for x in range(2, floor(num**0.5)+1):
        if num % x == 0:
            counter = counter + (x-1)
            num = num - (num//x)
            bln_get = True
            break
    if bln_get == False:
        counter = counter + (num - 1)
        num = num - 1 
print(counter)