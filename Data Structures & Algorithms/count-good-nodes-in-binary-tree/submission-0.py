# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        def dfs(node, hi):
            nonlocal res
            if node.val >= hi:
                res += 1
            hi = max(hi, node.val)
            if node.left:
                dfs(node.left, hi)
            if node.right:
                dfs(node.right, hi)
        
        dfs(root, hi=-float('inf'))
        return res
            