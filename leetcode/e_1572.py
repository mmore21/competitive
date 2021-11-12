"""
Problem: 1572 - Matrix Diagonal Sum
Difficulty: Easy
URL: https://leetcode.com/problems/matrix-diagonal-sum/
"""

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        s = 0
        for i in range(len(mat)):
            if i == len(mat)-1-i:
                s += mat[i][i]
            else:
                s += mat[i][i] + mat[len(mat)-1-i][i]
        return s