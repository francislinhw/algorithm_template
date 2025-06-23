# https://leetcode.com/problems/populating-next-right-pointers-in-each-node/description/
from collections import deque
from typing import Optional


# Definition for a Node.
class Node:
    def __init__(
        self,
        val: int = 0,
        left: Optional["Node"] = None,
        right: Optional["Node"] = None,
        next: Optional["Node"] = None,
    ):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: Optional[Node]) -> Optional[Node]:
        # 11.00
        # BFS
        if not root:
            return None

        queue = deque([root])

        while queue:
            prev = None
            size = len(queue)
            for _ in range(size):
                node = queue.popleft()
                if prev:
                    prev.next = node
                prev = node

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            # 最後一個節點 next 要是 None
            prev.next = None

        return root
