# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def checkTree(p2, q2):
            if not p2 and not q2:
                return True
            elif not p2 or not q2:
                return False
            elif p2.val == q2.val:
                return checkTree(p2.left, q2.left) and checkTree(p2.right, q2.right)
            else:
                return False
        return checkTree(p,q)
            
