import sys
def sieve(n):
    lst_primacity = [0 for j in range(n+1)]
    for x in range(2, n+1):
        if lst_primacity[x] == 0:
            for k in range(x, n+1, x):
                lst_primacity[k] += 1
    return(lst_primacity) 
    
lst_sieve = sieve(10000000)
n = int(sys.stdin.readline())
for gh in range(1, n+1):
    start, end, primacity = map(int, sys.stdin.readline().split())
    counter = 0 
    for jj in range(start, end + 1):
        if lst_sieve[jj] == primacity:
            counter+=1 
    print("Case #"+str(gh)+":", counter)
