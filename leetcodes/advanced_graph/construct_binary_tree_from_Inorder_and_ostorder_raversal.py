# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/

from typing import List, Optional

# inorder means left, root, right
# postorder means left, right, root
# 1. 後序最後一個是根節點
# 2. 根節點在中序中的位置
# 3. 先建右子樹（因為 postorder 是從右子樹往左 pop）
# 4. 再建左子樹
# 5. 返回根節點


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not postorder:
            return None

        # 後序最後一個是根節點
        root_val = postorder.pop()
        root = TreeNode(root_val)

        # 根節點在中序中的位置
        idx = inorder.index(root_val)

        # 先建右子樹（因為 postorder 是從右子樹往左 pop）
        root.right = self.buildTree(inorder[idx + 1 :], postorder)
        root.left = self.buildTree(inorder[:idx], postorder)

        return root
