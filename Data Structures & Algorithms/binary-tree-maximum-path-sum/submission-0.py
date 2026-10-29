# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # dfs of a node returns max of either going down left or right
        # plus itself
        maxSum = -float('inf')
        def dfs(node):
            if not node:
                return 0
            
            nonlocal maxSum
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            if not node.left and not node.right:
                maxSum = max(maxSum, node.val)
            elif not node.left and node.right:
                maxSum = max([maxSum, node.val, node.val + right])
            elif not node.right and node.left:
                maxSum = max([maxSum, node.val, node.val + left])
            else:
                maxSum = max([maxSum, node.val, node.val + right, node.val + left, node.val + right + left])
            
            return max([node.val, node.val + left, node.val + right])
        
        dfs(root)

        return maxSum
