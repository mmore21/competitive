"""
Problem 2149 - Rearrange Array Elements by Sign
Difficulty: Medium
URL: https://leetcode.com/problems/rearrange-array-elements-by-sign/
"""

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        neg = []
        pos = []
        res = []
        
        for i in range(len(nums)):
            if nums[i] > 0:
                pos.append(nums[i])
            else:
                neg.append(nums[i])
        
        for i in range(len(pos)):
            res.append(pos[i])
            res.append(neg[i])
        
        return res
