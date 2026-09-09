# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import sys
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        def oneMore(n1, n2, d):
            global depth
            if not n1 and not n2:
                depth = min(depth, d)
                return
            elif not n2:
                oneMore(n1.left, n1.right, d+1)
            elif not n1:
                oneMore(n2.left, n2.right, d+1)
            else:
                oneMore(n2.left, n2.right, d+1)
                oneMore(n1.left, n1.right, d+1)
            return
        global depth
        passDepth = 1
        depth = sys.maxsize
        oneMore(root.left, root.right, passDepth)
        return depth 