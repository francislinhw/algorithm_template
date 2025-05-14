# https://leetcode.com/problems/reorder-list/

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # # 1134
        # iterator = head
        # iterator2 = head
        # num = 0

        # pointerMap = {}

        # while iterator:
        #     pointerMap[num] = iterator
        #     iterator = iterator.next
        #     num += 1

        # print(pointerMap)

        # l = 0
        # r = num - 1

        # order = []

        # while l <= r:
        #     if l == r:
        #         order.append(l)
        #     else:
        #         order.append(l)
        #         order.append(r)
        #     l += 1
        #     r -= 1

        # for i in range(1, len(order), 1):
        #     toNode = pointerMap[order[i]]
        #     iterator2.next = toNode
        #     iterator2 = iterator2.next

        # iterator2.next = None

        # return head # 1153 1207
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        secondHead = slow.next
        slow.next = None
        prev = None

        while secondHead:
            secondHeadNext = secondHead.next
            secondHead.next = prev
            prev = secondHead
            secondHead = secondHeadNext

        temp = ListNode()
        h = temp
        l1 = head
        l2 = prev

        while l2:
            temp.next = l1
            temp = temp.next
            l1 = l1.next
            temp.next = l2
            temp = temp.next
            l2 = l2.next

        while l1:
            temp.next = l1
            l1 = l1.next

        return h.next


# 7 March Practice


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # 1134
        iterator = head
        iterator2 = head
        num = 0

        pointerMap = {}

        while iterator:
            pointerMap[num] = iterator
            iterator = iterator.next
            num += 1

        print(pointerMap)

        l = 0
        r = num - 1

        order = []

        while l <= r:
            if l == r:
                order.append(l)
            else:
                order.append(l)
                order.append(r)
            l += 1
            r -= 1

        for i in range(1, len(order), 1):
            toNode = pointerMap[order[i]]
            iterator2.next = toNode
            iterator2 = iterator2.next

        iterator2.next = None

        return head  # 1153 1207

    # Standard

    def reorderList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if not head:
            return head

        length = 0

        copyHead = head
        previousNode = None

        while copyHead:
            nextNode = copyHead.next
            copyHead.next = previousNode
            previousNode = copyHead
            if nextNode:
                copyHead = nextNode
                length += 1
            else:
                break

        lPtr = 0
        rPtr = length
        newNode = ListNode()
        temp = newNode

        while rPtr > lPtr:
            n = copyHead.val
            one = head.val
            newNode.val = n
            newNode.next = ListNode(one)
            newNode = newNode.next
            rPtr += 1
            lPtr -= 1

        return temp


# correct answer


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # In thie way, slow stops at the mid point of the Linkedlist

        secondHead = slow.next
        slow.next = None
        prev = None

        while secondHead:
            secondHeadNext = secondHead.next
            secondHead.next = prev
            prev = secondHead
            secondHead = secondHeadNext

        # Reverse the latter partof the linkedlist

        temp = ListNode()
        h = temp
        l1 = head
        l2 = prev

        while l2:
            temp.next = l1
            temp = temp.next
            l1 = l1.next
            temp.next = l2
            temp = temp.next
            l2 = l2.next

        while l1:  # handle the odd number case
            temp.next = l1
            l1 = l1.next
        # merge two of them
        return h.next
