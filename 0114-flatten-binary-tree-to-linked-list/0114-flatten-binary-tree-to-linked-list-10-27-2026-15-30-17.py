class Solution:
    def flatten(self, root: TreeNode | None) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return None
        res = TreeNode()          # dummy head
        returnRes = res
        def search(node):
            nonlocal res
            if not node:
                return
            res.right = TreeNode(node.val)   # right, not left
            res = res.right

            search(node.left)
            search(node.right)
        search(root)              # root, not res

        # returnRes.right is a copy of root, so its .right is the rest of the list
        root.left = None
        root.right = returnRes.right.right