"""
Problem: 1304 - Find N Unique Integers Sum up to Zero
Difficulty: Easy
URL: https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/
"""

class Solution:
    def sumZero(self, n: int) -> List[int]:
        num = 1
        arr = []
        
        if n % 2 != 0:
            arr.append(0)
            
        while len(arr) < n:
            arr.append(num)
            arr.append(-num)
            num += 1
            
                    
        return arr