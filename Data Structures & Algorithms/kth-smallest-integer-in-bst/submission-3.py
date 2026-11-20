# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        seen = []
        def dfs(node):
            if not node or len(seen) >= k:
                return
            dfs(node.left)
            if len(seen) < k:
                seen.append(node.val)
            dfs(node.right)
        dfs(root)
        return seen[k - 1]