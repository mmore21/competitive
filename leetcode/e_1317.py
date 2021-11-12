"""
Problem: 1317 - Convert Integer to the Sum of Two No-Zero Integers
Difficulty: Easy
URL: https://leetcode.com/problems/convert-integer-to-the-sum-of-two-no-zero-integers/
"""

class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        res = []
        hi = n - 1
        lo = 1
        while '0' in str(hi) or '0' in str(lo):
            hi -= 1
            lo += 1
            
        return [hi, n - hi]