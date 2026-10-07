# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        res = []
        def BFS(node, depth):
            if not node:
                return
            if depth == len(res):
                res.append([])
            res[depth].append(node.val)
            BFS(node.left, depth+1)
            BFS(node.right, depth+1)
        BFS(root, 0)
        return res
