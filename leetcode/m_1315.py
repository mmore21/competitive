"""
Problem: 1315 - Sum of Nodes with Even-Valued Grandparent
Difficulty: Medium
URL: https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/
"""

class Solution:
    def dfs(self, root, s=0):
        if root.val % 2 == 0:
            if root.left:
                if root.left.left:
                    s += root.left.left.val
                if root.left.right:
                    s += root.left.right.val
            if root.right:
                if root.right.left:
                    s += root.right.left.val
                if root.right.right:
                    s += root.right.right.val
                    
        if root.left:
            s = self.dfs(root.left, s)
        if root.right:
            s = self.dfs(root.right, s)
        
        return s
    
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        return self.dfs(root)