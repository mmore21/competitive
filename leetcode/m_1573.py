"""
Problem: 1573 - Number of Ways to Split a String
Difficulty: Medium
URL: https://leetcode.com/problems/number-of-ways-to-split-a-string/
"""

class Solution:
    def numWays(self, s: str) -> int:
        loc = []
        count = 0
        
        for i in range(len(s)):
            if s[i] == "1":
                count += 1
                loc.append(i)
        
        if count == 0:
            return factorial(len(s)-1) // (factorial(2) * factorial(len(s)-3)) % (10**9 + 7)
        if count % 3 != 0:
            return 0
        
        split = count // 3
            
        subs = []
        for i in range(3):
            subs.append(loc[i*split:(i+1)*split])
            print(subs)
        
        return (subs[2][0] - subs[1][-1]) * (subs[1][0] - subs[0][-1]) % (10**9 + 7)