"""
Problem: 4 - Largest Palindrome Product
URL: https://projecteuler.net/problem=4
"""

def largest_palindrome():
    m = 0
    for i in reversed(range(100, 1000)):
        for j in reversed(range(100, i)):
            p = i * j
            if p > m:
                if str(p) == str(p)[::-1]:
                    m = p
    return m

print(largest_palindrome())