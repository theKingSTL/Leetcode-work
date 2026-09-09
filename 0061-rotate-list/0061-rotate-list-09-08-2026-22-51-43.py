# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        node = head 
        lenNode = head
        if head == None:
            return head
        if head.next == None:
            return head
        length = 1
        while lenNode.next != None:
            lenNode = lenNode.next 
            length = length + 1
        print(length)
        newk = k%length 
        print(newk)
        if k == 0:
            return head
        for i in range(newk):
            while node.next != None:
                preNode = node
                node = node.next
            preNode.next = None
            node.next = head 
            head = node 
            prevNode = head 
        
        return node