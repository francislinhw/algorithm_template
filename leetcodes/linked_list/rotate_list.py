# https://leetcode.com/problems/rotate-list/description/

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head

        # Step 1: 計算長度
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1

        # Step 2: 取模處理
        k = k % length
        if k == 0:
            return head

        # Step 3: 找到新尾巴的位置（第 length - k 個節點）
        new_tail = head
        for _ in range(length - k - 1):
            new_tail = new_tail.next

        # Step 4: 重新連接
        tail.next = head
        new_head = new_tail.next
        new_tail.next = None

        return new_head
