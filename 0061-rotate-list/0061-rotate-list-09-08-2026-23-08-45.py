class Solution:
    def rotateRight(
        self,
        head: Optional[ListNode],
        k: int
    ) -> Optional[ListNode]:

        if head is None or head.next is None or k == 0:
            return head

        # Find the length and the final node
        tail = head
        length = 1

        while tail.next is not None:
            tail = tail.next
            length += 1

        rotations = k % length

        if rotations == 0:
            return head

        # Find the new tail
        new_tail = head

        for _ in range(length - rotations - 1):
            new_tail = new_tail.next

        new_head = new_tail.next

        # Connect the old tail to the old head,
        # then cut after the new tail
        tail.next = head
        new_tail.next = None

        return new_head