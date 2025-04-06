# https://leetcode.com/problems/count-good-nodes-in-binary-tree/

from collections import deque


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 4 Apr 2025
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        """
        :type root: TreeNode
        :rtype: int
        """

        # 7.37
        # DFS and pass though the max value in the path

        numberOfGood = [0]

        def dfs(node, maxInPath):
            if node.val < maxInPath:
                numberOfGood[0] += 0
            else:
                numberOfGood[0] += 1
            if node.left is not None:
                dfs(node.left, max(maxInPath, node.val))
            if node.right is not None:
                dfs(node.right, max(maxInPath, node.val))

        dfs(root, root.val)
        return numberOfGood[0]  # 9 min


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


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
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


"""

    def goodNodes(self, root: TreeNode) -> int:
        
        self.cnt = 0
        def dfs(node, preVal):
            if not node:
                return
            if node.val >= preVal:
                self.cnt += 1
            dfs(node.left, max(preVal, node.val))
            dfs(node.right, max(preVal, node.val))

        dfs(root, float('-inf'))
        return self.cnt

"""
