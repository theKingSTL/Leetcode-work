# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode | None) -> list[int]:
        res = []
        def depthSearch(node):
            if not node:
                return
            res.append(node.val)
            depthSearch(node.left)
            depthSearch(node.right)
        depthSearch(root)
        return res
