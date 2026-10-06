# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode | None) -> ListNode | None:
        res = head
        if not head:
            return None
        sortList = []
        while head:
            sortList.append(head.val)
            head = head.next
        sortList.sort()
        head = res
        for s in sortList:
            head.val = s
            head = head.next
        return res
