"""
Author: Soumil Ramesh Kulkarni
Date: 03.09.2024

Question:
Given a binary tree, determine if it is
height-balanced
.



Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: true
Example 2:


Input: root = [1,2,2,3,3,null,null,4,4]
Output: false
Example 3:

Input: root = []
Output: true
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def height(self, node):
        if not node:
            return 0
        return 1 + max(self.height(node.left), self.height(node.right))

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        leftheight = self.height(root.left)
        rightheight = self.height(root.right)

        return (abs(leftheight - rightheight) < 2 and self.isBalanced(root.left) and self.isBalanced(root.right))