# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good = 0
        def dfs(node, m):
            # m = max so far
            nonlocal good
            if not node:
                return

            if node.val >= m:
                good += 1

            m = max(m, node.val)
            dfs(node.left, m)
            dfs(node.right, m)

        dfs(root, -float('inf'))
        return good