N = int(input())
modulus = 1000000013
def fast_exponentiation(base, exp, mod):
    if exp == 0:
        return 1 
    elif exp == 1:
        return base
    else:
        R = fast_exponentiation(base, exp//2, mod)
        if exp%2 == 0:
            return ((R%mod)*(R%mod))%mod 
        else:
            return ((R%mod)*(R%mod)*(base))%mod
            
if N % 8 == 0:
    ans = fast_exponentiation(2, N//2 - 1, modulus)
    ans = ((ans%modulus)*((ans+1)%modulus))%modulus
    print(ans)
elif N % 8 == 1 or N % 8 == 7:
    if N == 1:
        print(1)
    else:
        ans = fast_exponentiation(2, (N-3)//2, modulus)
        ans = (fast_exponentiation(2, N-2, modulus)+ans)%modulus
        print(ans)
elif N % 8 == 2 or N % 8 == 6:
    ans = fast_exponentiation(2, N-2, modulus)
    print(ans)
elif N % 8 == 3 or N % 8 == 5:
    ans = fast_exponentiation(2, (N-3)//2, modulus)
    ans = (fast_exponentiation(2, N-2, modulus)-ans)%modulus
    print(ans)
else:
    ans = fast_exponentiation(2, N//2 - 1, modulus)
    ans = ((ans%modulus)*((ans-1)%modulus))%modulus
    print(ans)