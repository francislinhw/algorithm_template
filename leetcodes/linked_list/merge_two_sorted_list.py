# https://leetcode.com/problems/merge-two-sorted-lists/description/
from typing import Optional

# 7 March Practice


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        # 10.00
        if list1 is None and list2 is None:
            return None
        head = ListNode()
        pointer = head
        result = []

        while (list1 is not None) or (list2 is not None):  # O(n)
            # Case 1 list1 list2 are not None
            if (list1 is not None) and (list2 is not None):
                if list1.val <= list2.val:
                    result.append(list1.val)
                    list1 = list1.next
                else:
                    result.append(list2.val)
                    list2 = list2.next

            # Case list1 is None
            elif list1 is not None:
                result.append(list1.val)
                list1 = list1.next
            # Case list2 is None
            elif list2 is not None:
                result.append(list2.val)
                list2 = list2.next

        for i in range(len(result)):  # O(n)
            pointer.val = result[i]
            pointer.next = ListNode() if i < len(result) - 1 else None
            pointer = pointer.next

        return head
        # 10.34

    # fist try

    def mergeTwoListsPractice(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        # edge case
        if not list1 and not list2:
            return None

        if not list1:
            return list2

        if not list2:
            return list1

        returnList = ListNode()
        head = returnList

        while list1 and list2:
            if list1.val >= list2.val:
                returnList.next = list2  # key is to set the node at next
                list2 = list2.next

            elif list1.val < list2.val:
                returnList.next = list1  # key is to set the node at next
                list1 = list1.next

            returnList = returnList.next

        if list1:
            returnList.next = list1
        if list2:
            returnList.next = list2

        return head.next  # key is to set the node at next
