from sys import * 
N = int(stdin.readline())
mod = 1000000007
original_list = list(map(int, stdin.readline().split()))
M = int(stdin.readline())
    
def fast_expo(a, n, mod):
    if n == 0:
        return 1 
    elif n == 1:
        return a 
    else:
        split = fast_expo(a, n//2, mod)
        if n%2 == 0:
            return (split * split)%mod 
        else:
            return (split * split * a)%mod
        
list_of_multiples = [1, M]
multiplier = M
for i in range(N-2):
    multiplier = (multiplier * (M+i+1) * fast_expo(i+2, 1000000005, mod))%mod    
    list_of_multiples.append(multiplier)
output_list = []
for x in range(N):
    builder = original_list[x]
    for x2 in range(x):
        builder += (original_list[x2]*list_of_multiples[x-x2])%mod
    output_list.append(builder%mod)
print(*output_list)