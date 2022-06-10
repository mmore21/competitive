"""
Problem: 3 - Longest Substring Without Repeating Characters
Difficulty: Medium
URL: https://leetcode.com/problems/longest-substring-without-repeating-characters/
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0

        for i in range(len(s)):
            chars = set()

            for j in range(i, len(s)):
                if s[j] in chars:
                    break
                chars.add(s[j])

            if len(chars) > max_len:
                max_len =  len(chars)

        return max_len
