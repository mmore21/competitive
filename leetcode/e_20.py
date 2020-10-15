"""
Problem: 20 - Valid Parentheses
Difficulty: Easy
URL: https://leetcode.com/problems/valid-parentheses/
"""

class Solution:
    def isValid(self, s: str) -> bool:
        matching = {'(': ')', '{': '}', '[': ']'}
        stack = []
        
        for c in s:
            if c in "({[":
                stack.append(c)
            else:
                if len(stack) == 0 or c != matching[stack.pop()]:
                    return False
        
        return len(stack) == 0