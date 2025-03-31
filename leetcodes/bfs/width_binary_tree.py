# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import deque
from typing import Optional


# 31 March 2025 Practice
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # 11.30
        # BFS problem -> simple V (Choosen)
        # 2^level -> complicated X

        if not root:
            return 0

        max_width = 0
        # Each element in the queue is a tuple: (node, index)
        # The root node is given an index of 0.
        queue = deque([(root, 0)])

        while queue:
            level_length = len(queue)
            # Use the index of the first node in the current level as the offset.
            _, level_head_index = queue[0]
            # Example:
            # queue = [(1, 0)]
            # level_head_index = 0
            # level_length = 1
            # Round 2
            # queue = [(2, 0), (3, 1)]
            # level_head_index = 0
            # level_length = 2

            for i in range(level_length):
                # i = 0
                node, index = queue.popleft()
                # node = 1
                # index = 0
                # Normalize index to prevent overflow: subtract the offset
                normalized_index = index - level_head_index
                # normalized_index = 0 - 0 = 0
                # Round 2
                # node = 2
                # index = 0
                # normalized_index = 0 - 0 = 0
                # node = 3
                # index = 1
                # normalized_index = 1 - 0 = 1
                if node.left:
                    queue.append((node.left, 2 * normalized_index))
                    # queue = [(2, 0)]
                if node.right:
                    queue.append((node.right, 2 * normalized_index + 1))
                    # queue = [(2, 0), (3, 1)]
                # At the end of the level, compute the width
                if i == level_length - 1:
                    # i = 0
                    # level_length = 1
                    # normalized_index = 0
                    # normalized_index + 1 gives the width of this level
                    max_width = max(max_width, normalized_index + 1)
                    # max_width = max(max_width, 0 + 1)
                    # max_width = 1

        return max_width


# https://leetcode.com/problems/maximum-width-of-binary-tree/
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
