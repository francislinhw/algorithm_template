# https://leetcode.com/problems/partition-list/description/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # 10.07
        if not head:
            return None

        # Dummy heads
        smaller_head = ListNode(0)
        larger_head = ListNode(0)
        small = smaller_head
        large = larger_head

        while head:
            if head.val < x:
                small.next = head
                small = small.next
            else:
                large.next = head
                large = large.next
            head = head.next

        # Important: close the larger list
        large.next = None
        # Connect smaller list to larger list
        small.next = larger_head.next

        return smaller_head.next


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        before_head = ListNode(0)
        after_head = ListNode(0)
        before = before_head
        after = after_head

        current = head
        while current:
            if current.val < x:
                before.next = current
                before = before.next
            else:
                after.next = current
                after = after.next
            current = current.next

        after.next = None  # Important to terminate the list
        before.next = after_head.next

        return before_head.next
