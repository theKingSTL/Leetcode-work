class Solution:
    def partition(self, head: ListNode | None, x: int) -> ListNode | None:
        aTail, aHead, bTail, bHead = None, None, None, None
        cNode = head  
        while cNode:
            if cNode.val < x:
                if not bTail:
                    bTail = ListNode(cNode.val)
                    bHead = bTail
                else:
                    bTail.next = ListNode(cNode.val)
                    bTail = bTail.next
            else:
                if not aTail:
                    aTail = ListNode(cNode.val)
                    aHead = aTail
                else:
                    aTail.next = ListNode(cNode.val)
                    aTail = aTail.next
            cNode = cNode.next
        if not aTail:
            return bHead
        elif not bTail:
            return aHead
        else:
            bTail.next = aHead
        return bHead