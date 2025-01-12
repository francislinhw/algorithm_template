class Solution:
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        if not head:  # if head is None
            return False

        fast = head.next
        slow = head

        while fast and fast.next and slow:
            if fast == slow:
                return True
            fast = fast.next.next
            slow = slow.next

        return False