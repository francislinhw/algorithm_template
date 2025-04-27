# https://leetcode.com/problems/swap-nodes-in-pairs/


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # 6.54
        containers = []
        iterable = head
        while iterable:
            value = iterable.val
            containers.append(value)
            iterable = iterable.next

        def swap(items):
            for i in range(2, len(items) + 1, 2):
                temp = items[i - 1]
                items[i - 1] = items[i - 2]
                items[i - 2] = temp

            return items

        containers = swap(containers)

        if containers == []:
            return None

        print(containers)
        newHead = ListNode(0)
        loop = newHead

        for i in range(0, len(containers)):
            loop.val = containers[i]
            if i < len(containers) - 1:
                loop.next = ListNode(0)
                loop = loop.next

        return newHead


class Solution(object):
    def swapPairs(self, head):
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        while head and head.next:
            first = head
            second = head.next

            # Swap
            prev.next = second
            first.next = second.next
            second.next = first

            # Move pointers forward
            prev = first
            head = first.next

        return dummy.next
