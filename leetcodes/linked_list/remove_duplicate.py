# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 9.54
        handle = ListNode(None, head)

        prev = handle
        start = handle.next

        while start:
            if (
                start.val is not None
                and start.next is not None
                and start.val == start.next.val
            ):
                duplicate = start.val
                while start and start.val == duplicate:
                    start = start.next
            else:
                prev = prev.next
                start = start.next

            prev.next = start

        return handle.next  # 10.11 17min
