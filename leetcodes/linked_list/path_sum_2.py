# https://leetcode.com/problems/path-sum-ii/description/

from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        paths = []

        def dfs(node, path, curr_sum):
            if not node:
                return
            # 把當前節點加到 path 裡
            path.append(node.val)
            curr_sum += node.val
            # 葉節點且總和等於 targetSum
            if not node.left and not node.right and curr_sum == targetSum:
                paths.append(path[:])
            # 遞迴左右子樹
            dfs(node.left, path, curr_sum)
            dfs(node.right, path, curr_sum)
            # 回溯
            path.pop()

        dfs(root, [], 0)
        return paths
