# https://leetcode.com/problems/subtree-of-another-tree/
from collections import deque
from typing import Optional

# https://leetcode.com/problems/subtree-of-another-tree/

from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 31 Mar 2025 Practice


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False

        def compareTwoTree(n1, n2):
            if not n1 and not n2:
                return True
            if not n1 or not n2:
                return False
            if n1.val != n2.val:
                return False
            return compareTwoTree(n1.left, n2.left) and compareTwoTree(n1.right, n2.right)

        queue = deque([root])
        while queue:
            node = queue.popleft()
            if compareTwoTree(node, subRoot):
                return True
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return False


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: Optional[TreeNode]
        :type subRoot: Optional[TreeNode]
        :rtype: bool
        """

        def isTheSameNode(node1, node2):
            qIn1 = deque()
            qIn1.append(node1)
            qIn2 = deque()
            qIn2.append(node2)

            while qIn1 and qIn2:
                for i in range(len(qIn1)):
                    node1 = qIn1.popleft()
                    node2 = qIn2.popleft()

                    if node1.left and not node2.left:
                        return False
                    if not node1.left and node2.left:
                        return False
                    if node1.right and not node2.right:
                        return False
                    if not node1.right and node2.right:
                        return False

                    if node1.val != node2.val:
                        return False

                    if node1.left:
                        qIn1.append(node1.left)

                    if node1.right:
                        qIn1.append(node1.right)

                    if node2.left:
                        qIn2.append(node2.left)

                    if node2.right:
                        qIn2.append(node2.right)

                    if len(qIn1) != len(qIn2):
                        return False

            if qIn1:
                return False
            if qIn2:
                return False

            return True

        q = deque()
        q.append(root)

        while q:
            for i in range(len(q)):
                node = q.popleft()

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

                if isTheSameNode(node, subRoot):
                    return True

        return False


#
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        if not root:
            return False

        def sameTree(p, q):
            if not p and not q:
                return True
            if (not p and q) or (p and not q):
                return False
            if p.val != q.val:
                return False
            left = sameTree(p.left, q.left)
            right = sameTree(p.right, q.right)
            return left and right

        if root.val == subRoot.val:
            if sameTree(root, subRoot):
                return True

        left = self.isSubtree(root.left, subRoot)
        right = self.isSubtree(root.right, subRoot)
        return left or right


# root = [4, 5] subRoot = [4, null, 5] => False
root = TreeNode(4)
root.left = TreeNode(5)

subRoot = TreeNode(4)
subRoot.left = None
subRoot.right = TreeNode(5)

s = Solution()
print(s.isSubtree(root, subRoot))  # True d
