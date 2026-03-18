# Question: Given the root of a binary tree, return the sum of all node values.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional

class Solution:
    def sumNodes(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        left = self.sumNodes(root.left)
        right = self.sumNodes(root.right)

        return root.val + left + right
