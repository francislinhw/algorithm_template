# https://leetcode.com/problems/reverse-nodes-in-k-group/
class ListNode(object):

    def __init__(self, val=0, next=None):

        self.val = val
        self.next = next


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
