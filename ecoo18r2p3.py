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

for j in range(10):
    inp = list(map(int, input().split()))
    number = inp[0]
    occurences = inp[1]
    lst_sieve = sieve(number)
    for lrg_fact in range(number, 1, -1):
        if (lst_sieve[lrg_fact]):
            if number % lrg_fact == 0:
                count = 0
                while number % lrg_fact == 0:
                    number = number // lrg_fact
                    count += 1
                break
    occurences *= count
    counter = 0 
    incr = 0
    while counter < occurences:
        counter += 1 
        incr += 1
        if incr % lrg_fact == 0:
            copy = incr
            while copy % lrg_fact == 0:
                copy = copy // lrg_fact
                counter += 1
    print(incr * lrg_fact)