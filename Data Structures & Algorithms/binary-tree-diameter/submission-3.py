# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root):
        best = 0
        def dfs(node):
            nonlocal best
            if not node:
                return 0
            l, r = dfs(node.left), dfs(node.right)
            best = max(best, l + r)
            return 1 + max(l, r)
        dfs(root)
        return best