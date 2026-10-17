# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        stack = [[root]]
        level = 0
        while stack:
            level += 1
            new_level = []
            for node in stack.pop():
                if node.left:
                    new_level.append(node.left)
                if node.right:
                    new_level.append(node.right)
            if new_level:
                stack.append(new_level)
        
        return level
            
