# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        from collections import deque
        res = []
        d = deque([root])
        while d:
            for i in range(len(d)):
                node = d.popleft()
                level_right = node.val
                if node.left:
                    d.append(node.left)
                if node.right:
                    d.append(node.right)
            res.append(level_right)
        
        return res