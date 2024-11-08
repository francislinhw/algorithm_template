# https://leetcode.com/problems/count-good-nodes-in-binary-tree/

from collections import deque


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if not root:
            return []

        q = deque()
        q.append([root, root.val])
        goodNodes = 0

        while q:
            levelSize = len(q)

            for i in range(levelSize):
                node, maxVal = q.popleft()

                if node.val >= maxVal:
                    goodNodes += 1

                currentMax = max(maxVal, node.val)

                if node.left:
                    q.append((node.left, currentMax))
                if node.right:
                    q.append((node.right, currentMax))

        return goodNodes
