"""
Problem: 1448 - Count Good Nodes in Binary Tree
Difficulty: Medium
URL: https://leetcode.com/problems/count-good-nodes-in-binary-tree/
"""

class Solution:
    def dfs(self, node, max_val, count=0):  
        if node.val >= max_val:
            count += 1
            max_val = node.val
            
        if node.left:
            count = self.dfs(node.left, max_val, count)
        if node.right:
            count = self.dfs(node.right, max_val, count)
            
        return count
        
    def goodNodes(self, root: TreeNode) -> int:
        r, l = 0, 0
        if root.left:
            l = self.dfs(root.left, root.val)
        if root.right:
            r = self.dfs(root.right, root.val)
        return l + r + 1