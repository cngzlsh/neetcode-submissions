# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def isSame(a, b):
            if a and not b: return False
            if b and not a: return False
            if not a and not b: return True
            return a.val == b.val and isSame(a.left, b.left) and isSame(a.right, b.right)

        return isSame(p, q) 