# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        head = root
        if not root: return TreeNode(val)
        while head.left or head.right:
            if val < head.val and head.left:
                head = head.left
            elif val > head.val and head.right:
                head = head.right
            else:
                break
        
        if val < head.val:
            head.left = TreeNode(val)
        else:
            head.right = TreeNode(val)
        
        return root