# https://leetcode.com/problems/reverse-nodes-in-k-group/

from typing import Optional


class ListNode(object):

    def __init__(self, val=0, next=None):

        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse(start: ListNode, end: ListNode) -> ListNode:
            """
            反轉[start, end)這一段節點（左閉右開），回傳反轉後的「新頭」
            """
            prev, curr = end, start
            while curr != end:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            return prev  # 回傳新的頭

        dummy = ListNode(0)
        dummy.next = head
        group_prev = dummy

        while True:
            # 1. 找第k個節點（kth）作為這組的尾巴（反轉到這為止）
            kth = group_prev
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next
            group_next = kth.next  # 下一組的開頭

            # 2. 反轉這一組
            start = group_prev.next  # 本組的起點
            group_prev.next = reverse(start, group_next)  # 反轉本組，接上前面
            group_prev = start  # 本組反轉後的尾巴，準備開始下個分組


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0)  # 建立虛擬頭節點（避免操作 head 時出錯）
        dummy.next = head  # 虛擬頭連接原始 head
        group_prev = dummy  # 設定每一組反轉前的前一個節點

        while True:  # 持續處理每一組 k 個節點
            kth = group_prev  # 從 group_prev 開始找第 k 個節點
            for _ in range(k):
                kth = kth.next
                if not kth:  # 如果不足 k 個，直接結束
                    return dummy.next  # 回傳結果，因為最後這一組不用反轉
            group_next = kth.next  # kth（第k個）之後就是下一組的開頭

            # 開始反轉這一組 [group_prev.next, group_next)
            prev, curr = kth.next, group_prev.next  # prev 指向下一組的頭
            while curr != group_next:  # 只在這一組內反轉
                temp = curr.next  # 暫存下一節點
                curr.next = prev  # 反轉指標
                prev = curr  # prev 前進
                curr = temp  # curr 前進

            # 反轉結束後，將上一組的尾巴連接這組新的頭（kth），再把 group_prev 更新到這組的尾巴
            temp = group_prev.next  # 這時 temp 是這組反轉前的頭，反轉後會變成這組的尾巴
            group_prev.next = kth  # 將上一組的尾巴接到這組的頭（反轉後的 kth）
            group_prev = temp  # group_prev 更新到本組反轉後的尾巴，準備下一輪


# example
# Input: head = [1,2,3,4,5], k = 2
# Output: [2,1,4,3,5]

# Input: head = [1,2,3,4,5], k = 3
# Output: [3,2,1,4,5]

sol = Solution()
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
k = 2
result = sol.reverseKGroup(head, k)
print(result)


class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        # 檢查是否有足夠的節點可反轉
        count = 0
        ptr = head
        while ptr and count < k:
            ptr = ptr.next
            count += 1
        if count < k:
            return head

        # 反轉這 k 個節點
        prev = None
        curr = head
        for _ in range(k):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # head 現在是尾端，接上下一組反轉的結果
        head.next = self.reverseKGroup(curr, k)

        return prev


class Solution(object):
    def reverseKGroup(self, head, k):
        dummy = ListNode(0)
        dummy.next = head
        group_prev = dummy

        while True:
            # 找出這一組的第 k 個 node
            kth = self.get_kth_node(group_prev, k)
            if not kth:
                break
            group_next = kth.next

            # 反轉這一段
            prev, curr = kth.next, group_prev.next
            while curr != group_next:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            # 重新接起來
            temp = group_prev.next
            group_prev.next = kth
            group_prev = temp

        return dummy.next

    def get_kth_node(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr
