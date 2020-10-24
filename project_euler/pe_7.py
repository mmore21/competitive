"""
Problem: 7 - 10001st Prime
URL: https://projecteuler.net/problem=7
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

count = 1
num = 2

while count < 10001:
    num += 1
    if is_prime(num):
        count += 1

print(num)