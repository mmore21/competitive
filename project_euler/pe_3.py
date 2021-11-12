"""
Problem: 3 - Largest Prime Factor
URL: https://projecteuler.net/problem=3
"""

import math

def is_prime(num):
    if num > 2 and num % 2 == 0:
        return False
    else:
        for i in range(3, int(math.sqrt(num)) + 1, 2):
            if num % i == 0:
                return False
    return True

n = 600851475143
i = 2

while i * i < n:
    while n % i == 0:
        n = n // i
    i = i + 1
print(n)