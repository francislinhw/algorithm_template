# linked List

from collections import deque


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Node(object):
    def __init__(self, left=None, right=None, value=None):
        left = None
        right = None

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



    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        # edge cases
        # 1 both empty
        if not list1 and not list2:
            return None
        # 2 one of them empty
        if not list2:
            return list1
        if not list1:
            return list2
        # 3 normal case

        return_list = []  # ListNode(None)

        head = ListNode()
        temp = head  # pointer need to be fixed

        while list1 and list2:
            val1 = list1.val
            val2 = list2.val

            if val1 <= val2:
                head.next = list1
                head = head.next
                list1 = list1.next
            else:
                head.next = list2
                head = head.next
                list2 = list2.next

        if list1:
            head.next = list1

        if list2:
            head.next = list2

        return temp.next

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

    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        depth = 0

        if not root:
            return depth

        q = deque()
        q.append(root)

        while q:
            for i in range(len(q)):
                val = q.popleft()

                if val.left:
                    q.append(val.left)

                if val.right:
                    q.append(val.right)

            depth += 1

        return depth

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


# Reorder List
# Given a singly linked list L: L0→L1→…→Ln-1→Ln,
# reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

# sample input
# 1 -> 2 -> 3 -> 4 -> 5 -> None
# 1 -> 5 -> 2 -> 4 -> 3 -> None
list_node = Solution.ListNode(1)
list_node.next = Solution.ListNode(2)
list_node.next.next = Solution.ListNode(3)
list_node.next.next.next = Solution.ListNode(4)
list_node.next.next.next.next = Solution.ListNode(5)

a = Solution().reorderList(list_node)
print(a)

# Example of reverse linked list
# 1 -> 2 -> 3 -> 4 -> 5 -> None
# None <- 1 <- 2 <- 3 <- 4 <- 5

list_node = Solution.ListNode(1)
list_node.next = Solution.ListNode(2)
list_node.next.next = Solution.ListNode(3)
list_node.next.next.next = Solution.ListNode(4)
list_node.next.next.next.next = Solution.ListNode(5)

a = Solution().reverseList(list_node)
print(a)
