# https://leetcode.com/problems/reverse-linked-list/
from typing import Optional

# 6 March 2025 Practice


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 6 March 2025 0103

        temp = None
        prev = None
        iterator = head

        while iterator:
            # Step 1 remember next one
            temp = iterator.next

            # Step 2 point to the prev
            iterator.next = prev

            # Step 3 iterate
            prev = iterator
            if temp is not None:
                iterator = temp
            else:
                break

        return iterator  # 1.22 19 min


class Solution:

    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        cur = head
        prev = None

        while cur:
            nextNode = cur.next
            cur.next = prev
            prev = cur
            cur = nextNode

        return prev

    def reverseListPractice(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head:
            return head

        currentNode = head
        previousNode = None
        temp = currentNode

        while currentNode:
            nextNode = currentNode.next
            currentNode.next = previousNode
            previousNode = currentNode
            if nextNode is not None:
                currentNode = nextNode
            else:
                break

        return currentNode  # which one should be returned?
