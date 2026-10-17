# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(self, root, subRoot):
        def same(a, b):
            if not a and not b: return True
            if not a or not b: return False
            return a.val == b.val and same(a.left, b.left) and same(a.right, b.right)

        def dfs(node):
            if not node: return False
            return same(node, subRoot) or dfs(node.left) or dfs(node.right)

        return dfs(root)