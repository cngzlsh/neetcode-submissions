# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        max_dia = 0
        # diameter is just the maxmimum of left depth + right depth
        def dfs(node):
            # returns the depth of a node
            if not node:
                return 0
            
            left, right = dfs(node.left), dfs(node.right)
            nonlocal max_dia
            max_dia = max(max_dia, left + right)

            return 1 + max(left, right)
        
        dfs(root)
        return max_dia