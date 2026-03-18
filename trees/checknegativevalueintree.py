# Question: Given the root of a binary tree, return True if any node has a negative value.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional

class Solution:
    def hasNegative(self, root: Optional[TreeNode]) -> bool:

        if not root:
            return False

        if root.val < 0:
            return True

        return self.hasNegative(root.left) or self.hasNegative(root.right)
