# https://leetcode.com/problems/sum-root-to-leaf-numbers/
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(node, cur_sum):
            if not node:
                return 0
            cur_sum = cur_sum * 10 + node.val
            if not node.left and not node.right:
                return cur_sum
            return dfs(node.left, cur_sum) + dfs(node.right, cur_sum)

        return dfs(root, 0)


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        # 11.42

        # DFS
        res = []

        def dfs(node: TreeNode, number: []):

            val = node.val
            number.append(val)
            if node.left is None and node.right is None:
                res.append(number)
                return

            if node.left is not None:
                next = node.left
                dfs(next, number[:])

            if node.right is not None:
                next = node.right
                dfs(next, number[:])

        dfs(root, [])

        result = 0

        for n in res:
            digit = len(n) - 1
            for d in n:
                result += d * 10 ** (digit)
                digit -= 1

        return result
