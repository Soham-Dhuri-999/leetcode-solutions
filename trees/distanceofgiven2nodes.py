# Question: Given the root of a binary tree, return the distance between two given nodes.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findDistance(self, root: Optional[TreeNode], p: int, q: int) -> int:
        distance = 0

        def dfs(node):
            nonlocal distance

            if not node:
                return -1

            left = dfs(node.left)
            right = dfs(node.right)

            
            if node.val == p or node.val == q:
                
                if left != -1:
                    distance = left + 1
                if right != -1:
                    distance = right + 1
                return 0

            
            if left != -1 and right != -1:
                distance = left + right + 2
                return -1  

            
            if left != -1:
                return left + 1
            if right != -1:
                return right + 1

            return -1

        dfs(root)
        return distance