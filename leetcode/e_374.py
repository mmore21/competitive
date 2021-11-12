"""
Problem: 374 - Guess Number Higher or Lower
Difficulty: Easy
URL: https://leetcode.com/problems/guess-number-higher-or-lower/
"""

class Solution:
    def guessNumber(self, n: int) -> int:
        lo = 0
        hi = n
        while lo <= hi:
            mid = (hi + lo) // 2
            res = guess(mid)
            if res == 0:
                return mid
            elif res > 0:
                lo = mid + 1
            else:
                hi = mid - 1
        return -1