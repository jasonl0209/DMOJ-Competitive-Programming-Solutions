import sys 
def sieve(n):
    lst_prime = [True for j in range(n+1)]
    x = 2
    while x * x <= n:
        if lst_prime[x] == True:
            for k in range(x*2, n+1, x):
                lst_prime[k] = False
        x+=1
    lst_prime[0] = False 
    lst_prime[1] = False
    return lst_prime

n = int(sys.stdin.readline())
lst_soe = sieve(1000000)
lst_macro_start = []
lst_macro_end = []
lst_macro_out = []
for k in range(n):
    inp = list(map(int, sys.stdin.readline().split()))
    start = inp[0]
    end = inp[1]
    lst_macro_start.append(start)
    lst_macro_end.append(end)
    counter = 0
    if k > 0:
        if lst_macro_start[k-1] == start and lst_macro_end[k-1] == end:
            counter = lst_macro_out[k-1]
            lst_macro_out.append(counter)
            print(counter)
        else:
            for i in range(start, end):
                if lst_soe[i] == True:
                    counter += 1
            lst_macro_out.append(counter)
            print(counter)
    else:
        for i in range(start, end):
            if lst_soe[i] == True:
                counter += 1
        lst_macro_out.append(counter)
        print(counter)