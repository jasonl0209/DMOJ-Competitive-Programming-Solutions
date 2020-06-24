#Author: Jason Lu (DMOJ Account: dmoj.ca/user/hfanalytica)
#Problem Link: dmoj.ca/problem/seq1
#Tags: Intermediate Math
#Concepts: Binary Exponentiation
#Time Complexity: O(log(N)), Space Complexity: O(1 

"""
Problem Analysis:

Let's observe the first few cases: N = [0, 1, 2, 3, 4] & K(N) = [3, 11, 27, 59, 123], wehere K(N) is the number of keystrokes for N 
Finding the first differences yield: [8, 16, 32, 64]; these are consecutive powers of 2. 
It is then reasonable to conclude that K(N)=  2^(N±X) - Y
Through further testing, we find this following pattern: K(N) = 2^(N+3) - 5
Therefore, the output is: 2^(N+3) - 5 mod 10^9 + 7

Implementation Analysis:

This seems straight forward; however, in order for the program to run under 0.42 seconds per case, with max(N) < 2^63, it cannot be fully solved through brute force exponentiation, since that runs in O(N) time. 
A neat trick with Python would be using the pow() function for quick exponentiation. This works; however, it still is not the most efficient solution. 
We could instead choose to implement an efficient binary exponentiation function, as shown below.

"""
import sys
modulo = 1000000007
def binary_exponentiation(base, exponent, mod):
    if exponent == 0:
        return 1 
    elif exponent == 1:
        return base
    else:
        split = binary_exponentiation(base, exponent//2, modulo)
        if exponent % 2 == 0:
            return (split * split) % mod 
        else:
            return (split * split * base) % mod
N = int(sys.stdin.readline())
keystrokes = (binary_exponentiation(2, N+3, modulo) - 5) % modulo
print(keystrokes)
