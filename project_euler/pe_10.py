"""
Problem: 10 - Summation of Primes
URL: https://projecteuler.net/problem=10
"""

import math

n = 2000000

def is_prime(num):
    if num > 2 and num % 2 == 0:
        return False
    else:
        for i in range(3, int(math.sqrt(num)) + 1, 2):
            if num % i == 0:
                return False
    return True

sum = 0
for x in range(2, n):
    if is_prime(x):
        sum += x
print(sum)