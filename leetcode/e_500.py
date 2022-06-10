"""
Problem: 500 - Keyboard Row
Difficulty: Easy
URL: https://leetcode.com/problems/keyboard-row/
"""

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        rows = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
        
        res = []
        for word in words:
            valid = True
            c = word[0].lower()
            if c in rows[0]:
                row = 0
            elif c in rows[1]:
                row = 1
            elif c in rows[2]:
                row = 2
                
            for i in range(1, len(word)):
                c = word[i].lower()
                if c not in rows[row]:
                    valid = False

            if valid:
                res.append(word)
                    
        return res

