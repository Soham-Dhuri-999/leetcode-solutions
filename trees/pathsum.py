# Question: Return true if the tree has a root-to-leaf path where all values sum to
# targetSum.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def dfs(node, remaining_sum):

            if not node:
                return False

            if not node.left and not node.right:
                return remaining_sum == node.val

            remaining_sum -= node.val

            return dfs(node.left, remaining_sum) or dfs(node.right, remaining_sum)

        return dfs(root, targetSum)
