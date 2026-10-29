# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def innerDfs(node, subroot):
            if not node and not subroot:
                return True
            if (not node and subroot) or (not subroot and node):
                return False
            if node.val != subroot.val:
                return False
            
            return innerDfs(node.left, subroot.left) and innerDfs(node.right, subroot.right)
        
        def outerDfs(root):
            if not root:
                return False
            if innerDfs(root, subRoot):
                return True
            
            if outerDfs(root.left) or outerDfs(root.right): return True
            return False
        
        return outerDfs(root)
