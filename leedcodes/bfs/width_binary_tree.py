# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import deque
from typing import Optional


class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        width = 0
        q = deque()
        q.append((root, 1))  #

        while q:
            minNum = float("inf")
            for i in range(len(q)):
                node, num = q.popleft()
                if not node:
                    continue
                q.append((node.left, num * 2))
                q.append((node.right, num * 2 + 1))
                minNum = min(minNum, num)
                width = max(width, num - minNum + 1)

        return width
