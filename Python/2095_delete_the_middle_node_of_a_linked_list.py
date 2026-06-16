class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head is None or head.next is None:
            return None
        slow_pointer = head
        prev_pointer = None
        fast_pointer = head
        while fast_pointer and fast_pointer.next:
            prev_pointer = slow_pointer
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next

        prev_pointer.next = slow_pointer.next
        return head
