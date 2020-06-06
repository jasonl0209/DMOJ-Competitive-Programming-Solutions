import sys
mod = 1000000007
def exp_squaring(a,n):
    if n == 0:
        return 1 
    elif n == 1:
        return a 
    else:
        split = exp_squaring(a,n//2)
        if n%2 == 0:
            return (split * split)%mod 
        else:
            return (split * split * a)%mod
n = int(sys.stdin.readline())
j = exp_squaring(2,n+3) - 5
print(j%mod)