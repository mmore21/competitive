
"""
Problem: 1629 - Slowest Key
Difficulty: Easy
URL: https://leetcode.com/problems/slowest-key/
"""

class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        max_time = 0
        lex = None
        
        for i in range(len(releaseTimes)):
            res = 0
            if i-1 < 0:
                res = releaseTimes[i]
            else:
                res = releaseTimes[i] - releaseTimes[i-1]
            
            if res == max_time:
                if keysPressed[i] > lex:
                    lex = keysPressed[i]
            elif res > max_time:
                max_time = res
                lex = keysPressed[i]
        
        return lex