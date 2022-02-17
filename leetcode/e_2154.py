"""
Problem 2154 - Keep Multiplying Found Values by Two
Difficulty: Easy
URL: https://leetcode.com/problems/keep-multiplying-found-values-by-two/
"""

class Solution:
    def bsearch(self, target, nums):
        while nums:
            idx = len(nums) // 2
            if target == nums[idx]:
                return True
            elif target < nums[idx]:
                nums = nums[:idx]
            else:
                nums = nums[idx+1:]
        return False
    
    def findFinalValue(self, nums: List[int], original: int) -> int:
        sorted_nums = sorted(nums)
        
        while original:
            if self.bsearch(original, sorted_nums):
                original *= 2
            else:
                break
            
        return original
