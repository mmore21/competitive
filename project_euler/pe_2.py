"""
Problem: 2 - Even Fibonacci Numbers
URL: https://projecteuler.net/problem=2
"""

def fib(limit):
    a, b = 0, 1
    while a < limit:
        if not a % 2:         
            yield a
        a, b = b, a + b

print(sum(fib(4000000)))