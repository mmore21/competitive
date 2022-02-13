"""
Problem 2165 - Smallest Value of the Rearranged Number
Difficulty: Medium
URL: https://leetcode.com/problems/smallest-value-of-the-rearranged-number/
"""

class Solution:
    def smallestNumber(self, num: int) -> int:
        if num > 0:
            digits = sorted([d for d in str(num)])
            i = 0
            while i < len(digits):
                if digits[i] != '0':
                    n = digits.pop(i)
                    digits.insert(0, n)
                    break
                i += 1
            res = int("".join(digits))
            return res
        elif num < 0:
            digits = list(reversed(sorted([d for d in str(num)[1:]])))
            res = int("".join(digits)) * -1
            return res
        
        return 0
