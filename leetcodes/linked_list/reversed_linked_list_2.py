# https://leetcode.com/problems/reverse-linked-list-ii/
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(
        self, head: Optional[ListNode], left: int, right: int
    ) -> Optional[ListNode]:
        # Step 0: Create a dummy node to simplify edge cases
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        # Step 1: Move `prev` to the node just before `left`
        for _ in range(left - 1):
            prev = prev.next

        # Now, `prev` is pointing to the node before the reversal starts
        # `curr` is the first node to be reversed
        curr = prev.next
        prev_sublist = None
        tail = curr  # Will become the tail of the reversed sublist

        # Step 2: Reverse the sublist between left and right
        for _ in range(right - left + 1):
            next_temp = curr.next
            curr.next = prev_sublist
            prev_sublist = curr
            curr = next_temp

        # Step 3: Connect reversed sublist back to the main list
        prev.next = prev_sublist
        tail.next = curr

        return dummy.next


class Solution:
    def reverseBetween(
        self, head: Optional[ListNode], left: int, right: int
    ) -> Optional[ListNode]:
        # Step 0: Dummy node to handle edge cases
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        # Step 1: Move prev to node before `left`
        for _ in range(left - 1):
            prev = prev.next

        # Step 2: Reverse sublist
        curr = prev.next
        for _ in range(right - left):
            temp = curr.next
            curr.next = temp.next
            temp.next = prev.next
            prev.next = temp

        return dummy.next
