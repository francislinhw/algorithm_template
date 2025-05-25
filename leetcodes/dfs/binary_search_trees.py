# https://leetcode.com/problems/unique-binary-search-trees-ii/description/
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        if n == 0:
            return []

        def dfs(start, end):
            trees = []
            if start > end:
                trees.append(None)
                return trees

            for i in range(start, end + 1):
                left_subtrees = dfs(start, i - 1)
                right_subtrees = dfs(i + 1, end)
                for l in left_subtrees:
                    for r in right_subtrees:
                        root = TreeNode(i)
                        root.left = l
                        root.right = r
                        trees.append(root)
            return trees

        return dfs(1, n)
