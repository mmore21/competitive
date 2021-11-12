"""
Problem: 6 - Sum Square Difference
URL: https://projecteuler.net/problem=6
"""

sum_square = sum([i ** 2 for i in range(1, 101)])
square_sum = sum([i for i in range(1, 101)]) ** 2

print(square_sum - sum_square)