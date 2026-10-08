# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        res = []
        def BFS(node):
            if not node:
                return
            else:
                BFS(node.left)
                res.append(node.val)
                BFS(node.right)
        BFS(root)
        return res
