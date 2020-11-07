"""
Problem: 136 - Single Number
Difficulty: Easy
URL: https://leetcode.com/problems/single-number/
"""

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        qty = defaultdict(int)
        
        for n in nums:
            qty[n] += 1
        
        for k, v in qty.items():
            if v == 1:
                return k
        return -1