# https://leetcode.com/problems/recover-binary-search-tree/

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # 8.20
        # 初始化三個指標
        self.first = self.second = self.prev = None

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            # 檢查中序遞增性，找逆序點
            if self.prev and self.prev.val > node.val:
                if not self.first:
                    self.first = self.prev
                self.second = node
            self.prev = node
            inorder(node.right)

        self.prev = None
        inorder(root)
        # 交換兩個異常節點的值
        if self.first and self.second:
            self.first.val, self.second.val = self.second.val, self.first.val
