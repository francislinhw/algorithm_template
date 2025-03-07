# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


from typing import Optional

# 6 March 2025 Practice


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # 12.45

        turtle = head
        if head is not None:
            hare = head.next

        # one jump one, the other jump 2
        while turtle is not None and hare is not None:
            if turtle == hare:
                return True

            turtle = turtle.next
            hare = hare.next
            if hare is not None:
                hare = hare.next

        return False  # 12.55


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
