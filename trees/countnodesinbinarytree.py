# Question: Given the root of a binary tree, return the total number of nodes.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional

class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        left = self.countNodes(root.left)
        right = self.countNodes(root.right)

        return 1 + left + right
