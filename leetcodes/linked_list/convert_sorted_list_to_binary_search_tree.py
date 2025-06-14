# https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/description/

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        # 11.56
        # base case: none
        if not head:
            return None

        # base case: only one
        if not head.next:
            return TreeNode(head.val)

        # 使用快慢指針找中間節點（slow 最終會指向中間節點）
        prev = None
        slow = head
        fast = head

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        # 切斷左半邊
        if prev:
            prev.next = None

        root = TreeNode(slow.val)
        root.left = self.sortedListToBST(head if slow != head else None)
        root.right = self.sortedListToBST(slow.next)

        return root
