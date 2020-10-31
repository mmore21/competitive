"""
Problem: 1630 - Arithmetic Subarrays
Difficulty: Medium
URL: https://leetcode.com/problems/arithmetic-subarrays/
"""

class Solution:
    
    def is_valid_subarray(self, sub):
        diff = None
        for i in range(len(sub) - 1):
            d = sub[i+1] - sub[i]
            if diff == None:
                diff = d
            elif diff != d:
                return False
        return True
    
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        m = len(l)
        res = []
        
        for i in range(m):
            sub = sorted(nums[l[i] : r[i]+1])                 
            res.append(self.is_valid_subarray(sub))
            
        return res