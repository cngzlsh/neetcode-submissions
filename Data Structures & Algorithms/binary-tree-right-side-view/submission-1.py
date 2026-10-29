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
        q = deque([root])
        res = []
        while q:
            new_level = deque()
            res_level = []
            for _ in range(len(q)):
                node = q.popleft()
                res_level.append(node.val)
                if node.left:
                    new_level.append(node.left)
                if node.right:
                    new_level.append(node.right)
            
            res.append(res_level[-1])
            q = new_level
        
        return res