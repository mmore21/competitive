"""
Problem: 1002 - Find Common Characters
Difficulty: Easy
URL: https://leetcode.com/problems/find-common-characters/
"""

class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        common = list(A[0])
        
        for word in A:
            curr = []
            for c in word:
                if c in common:
                    curr.append(c)
                    common.remove(c)
            common = curr
        
        return common