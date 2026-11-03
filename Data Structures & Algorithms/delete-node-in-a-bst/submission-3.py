class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:                                   # empty tree
            return None

        head = root

        # case 1: the root itself is deleted
        if head.val == key:
            if head.right:
                head2 = head.right
                while head2.left:
                    head2 = head2.left
                head2.left = head.left                 # hang left subtree under leftmost of right
                return head.right
            return head.left                           # only a left child, or a leaf (None)

        # find the PARENT of the node to delete
        while head:
            if head.left and head.left.val == key:
                break
            if head.right and head.right.val == key:
                break
            head = head.left if key < head.val else head.right

        if not head:                                   # key not in the tree
            return root

        # case 2: the node to delete is head.left
        if head.left and head.left.val == key:
            node = head.left
            if node.right:
                head2 = node.right
                while head2.left:
                    head2 = head2.left
                head2.left = node.left
                head.left = node.right
            else:
                head.left = node.left                  # covers left-only and leaf

        # case 3: the node to delete is head.right
        else:
            node = head.right
            if node.right:
                head2 = node.right
                while head2.left:
                    head2 = head2.left
                head2.left = node.left
                head.right = node.right
            else:
                head.right = node.left

        return root