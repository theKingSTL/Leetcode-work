# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode | None) -> TreeNode | None:
        res = []
        while head:
            res.append(head.val)
            head = head.next
        def turnArrayToBST(nums):
            if not nums:
                return None
            mid = len(nums) // 2
            return TreeNode(
                nums[mid],
                turnArrayToBST(nums[:mid]),
                turnArrayToBST(nums[mid + 1:]),
            )
        return turnArrayToBST(res)

        