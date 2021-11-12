"""
Problem: 1318 - Minimum Flips to Make a OR b Equal to c
Difficulty: Medium
URL: https://leetcode.com/problems/minimum-flips-to-make-a-or-b-equal-to-c/
"""

class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        a = bin(a)[2:]
        b = bin(b)[2:]
        c = bin(c)[2:]
        
        l = max(len(a), max(len(b), len(c)))
        
        if len(a) < l:
            a = a.zfill(l)
        if len(b) < l:
            b = b.zfill(l)
        if len(c) < l:
            c = c.zfill(l)
        
        count = 0

        for i in range(l):
            if c[i] == '0':
                count += int(a[i] != c[i]) + int(b[i] != c[i])
            else:
                count += int(a[i] != c[i]) * int(b[i] != c[i])
        
        return count