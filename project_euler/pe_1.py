"""
Problem: 1 - Multiples of 3 and 5
URL: https://projecteuler.net/problem=1
"""

print(sum(x for x in range(0, 1000) if x % 3 == 0 or x % 5 == 0))