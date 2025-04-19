from typing import Optional

# https://leetcode.com/problems/add-two-numbers/


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry
            carry = total // 10
            curr.next = ListNode(total % 10)
            curr = curr.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next


# 13 Apr 2025
class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        # 8.58
        # Step 1: Retore the value of l1 l2 and sum
        # Step 2: Make the LinkedList

        if not l1:
            return l2
        if not l2:
            return l1
        if not l1 and not l2:
            return ListNode(0)

        def getFigure(linkedList: Optional[ListNode]) -> int:
            figure = 0
            curr = linkedList
            digit = 0
            while curr:
                curVal = curr.val
                figure += (10**digit) * curVal
                curr = curr.next
                digit += 1
            return figure

        figure1 = getFigure(l1)
        figure2 = getFigure(l2)

        final = str(figure1 + figure2)
        finalLength = len(final)

        res = ListNode(0)
        head = res
        counter = 1
        for num in reversed(final):
            res.val = int(num)
            if finalLength != counter:
                res.next = ListNode(0, None)
                res = res.next
            counter += 1

        return head  # 16 min
