# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        max_diameter = 0

        def dfs(node):
            nonlocal max_diameter

            if not node:
                return 0

            if node.left:
                left = 1 + dfs(node.left)
            else:
                left = 0
            if node.right:
                right = 1 + dfs(node.right)
            else:
                right = 0
            
            max_diameter = max(max_diameter, left+right)
            return max(left, right)
        
        dfs(root)
        return max_diameter