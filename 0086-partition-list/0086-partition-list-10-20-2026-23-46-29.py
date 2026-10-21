# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode | None, x: int) -> ListNode | None:
        #Org list 
        #before list 
        #after list 
        #if node.val < x appen before
        #else append to after
        #append at end together 
        nodesAfter = None
        returnNodesAfter = None
        nodesBefore = None
        returnNodesBefore = None
        nodeCurrent = head
        while nodeCurrent:
            if nodeCurrent.val < x:
                if not nodesBefore:
                    nodesBefore = ListNode(nodeCurrent.val)
                    returnNodesBefore = nodesBefore
                else:
                    nodesBefore.next = ListNode(nodeCurrent.val)
                    nodesBefore = nodesBefore.next
            else:
                if not nodesAfter:
                    nodesAfter = ListNode(nodeCurrent.val)
                    returnNodesAfter = nodesAfter
                else:
                    nodesAfter.next = ListNode(nodeCurrent.val)
                    nodesAfter = nodesAfter.next
            nodeCurrent = nodeCurrent.next
        #stitch, possibl error
        if not nodesAfter:
            return returnNodesBefore
        elif not nodesBefore:
            return returnNodesAfter
        else:
            nodesBefore.next = returnNodesAfter
        return returnNodesBefore

        # nodesAfter = ListNode()
        # returnNodesAfter = nodesAfter
        # nodesBefore = ListNode()
        # returnNodesBefore = nodesBefore

        