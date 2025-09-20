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
        # 3.50

        node = ListNode(None, ListNode(None))
        handle = node

        node = node.next

        accumDigit = 0
        sumDigit = 0
        prevDigit = 0
        tail = None

        while l1 is not None or l2 is not None or prevDigit != 0:
            v1 = l1.val if l1 is not None else 0
            v2 = l2.val if l2 is not None else 0
            if (v1 + v2 + prevDigit) >= 10:
                accumDigit = 1
                sumDigit = v1 + v2 + prevDigit - 10
            else:
                sumDigit = v1 + v2 + prevDigit
                accumDigit = 0

            node.val = sumDigit
            tail = node
            node.next = ListNode(None)
            node = node.next
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next

            prevDigit = 1 if accumDigit > 0 else 0

        tail.next = None

        return handle.next  # 21 mines


class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode(0)
        node = dummy.next = ListNode(None)  # 你的風格：先留第一個可填的節點
        carry = 0

        while l1 or l2 or carry:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            s = x + y + carry
            carry = s // 10
            node.val = s % 10

            # 先移動指標與決定下一圈是否存在
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            if l1 or l2 or carry:  # 只有「還有下一圈」才建立下一個節點
                node.next = ListNode(None)
                node = node.next

        return dummy.next


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
