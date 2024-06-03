"""
Author: Soumil Ramesh Kulkarni
Date: 03.31.2024

Question:
Given the root of a binary tree, invert the tree, and return its root.

Example 1:
Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]

Example 2:
Input: root = [2,1,3]
Output: [2,3,1]

Example 3:
Input: root = []
Output: []
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import *
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Iterative Solution
        # Using BFS
        if root is None:
            return None
        queue = []
        queue.append(root)
        while queue:
            temp_node = queue.pop(0)
            # Swap The left and the right Subtrees
            temp_node.left, temp_node.right = temp_node.right, temp_node.left

            # Insert the the left and the right Subtrees if Present
            if temp_node.left:
                queue.append(temp_node.left)

            if temp_node.right:
                queue.append(temp_node.right)
        return root
