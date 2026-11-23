# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(node, curr_max, curr_min):
            # left must be smaller
            if not node:
                return True
            if node.val >= curr_max or node.val <= curr_min:
                return False

            return dfs(node.right, curr_max=curr_max, curr_min=max(curr_min, node.val)) and dfs(node.left, curr_max=min(curr_max, node.val), curr_min=curr_min)

        return dfs(root, curr_max=float('inf'), curr_min=float('-inf'))