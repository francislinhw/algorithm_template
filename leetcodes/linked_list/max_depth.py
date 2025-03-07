# Definition for a binary tree node.

from typing import Optional

from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 7 March 25 Practice
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # 12.20
        if root is None:
            return 0

        q = deque([[root]])

        layer = 0

        while q:
            elements = q.pop()
            if elements == []:
                break
            layer += 1

            nextElement = []
            for node in elements:
                if node.left is not None:
                    nextElement.append(node.left)
                if node.right is not None:
                    nextElement.append(node.right)

            q.append(nextElement)

        return layer


class Node(object):
    def __init__(self, left=None, right=None, value=None):
        left = None
        right = None

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
