# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        def oneMore(n1, n2, d):
            global depth
            if not n1 and not n2:
                return
            elif not n2:
                depth = max(depth, d+1)
                oneMore(n1.left, n1.right, d+1)
            elif not n1:
                depth = max(depth, d+1)
                oneMore(n2.left, n2.right, d+1)
            else:
                depth = max(depth, d+1)
                oneMore(n2.left, n2.right, d+1)
                oneMore(n1.left, n1.right, d+1)
            return
        global depth
        depth = 1
        oneMore(root.left, root.right, depth)
        return depth 