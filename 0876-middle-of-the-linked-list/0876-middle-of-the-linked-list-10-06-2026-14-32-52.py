# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        slowHead = head 
        fastHead = head
        while fastHead and fastHead.next:
            slowHead = slowHead.next
            fastHead = fastHead.next.next
        return slowHead
        