# https://leetcode.com/problems/binary-tree-level-order-traversal-ii/

from collections import deque
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        # 1. 处理空树
        if not root:
            return []

        res = []
        q = deque([root])

        # 2. 层序遍历
        while q:
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                level.append(node.val)
                # 3. 正确地把左右子节点加入队列
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            # 4. 把本层结果加入 res
            res.append(level)

        # 5. 最后自底向上返回
        return res[::-1]
