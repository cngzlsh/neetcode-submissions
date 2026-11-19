# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def dfs(node):
            if not node:
                return False
            
            if isIdentical(node, subRoot):
                return True
            
            return dfs(node.left) or dfs(node.right)

        def isIdentical(node, subRoot):
            if not node and not subRoot:
                return True
            if (node and not subRoot) or (not node and subRoot):
                return False
            
            if node.val != subRoot.val:
                return False
            
            return isIdentical(node.left, subRoot.left) and isIdentical(node.right, subRoot.right)
        

        return dfs(root)