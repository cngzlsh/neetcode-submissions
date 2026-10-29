# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        # O(n^2)
        # if not preorder or not inorder: 
        #     return None

        # root = TreeNode(preorder[0])
        # # first number in preorder is always a root
        # # that number in inorder tells us how to partition left and right subtree
        # mid = inorder.index(preorder[0])
        # root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        # root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        
        # return root
        
        
        pos = {v: i for i, v in enumerate(inorder)}   # value -> inorder index (values are unique)
        self.pre = 0                                  # next preorder index to use

        def build(lo, hi):                            # inorder range [lo, hi]
            if lo > hi:
                return None
            root = TreeNode(preorder[self.pre])
            self.pre += 1
            mid = pos[root.val]
            root.left = build(lo, mid - 1)            # left BEFORE right
            root.right = build(mid + 1, hi)
            return root

        return build(0, len(inorder) - 1)