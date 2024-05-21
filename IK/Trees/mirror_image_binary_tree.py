"""
Author: Soumil Ramesh Kulkarni
Date: 02.24.2024

Question:

Given the root of a binary tree, transform the tree in-place into its mirror image.

Example
        0
      /   \
    1        2
   /  \   /   \
  3    4  5    6
Output:

         0
      /    \
    2         1
   /  \    /   \
  6    5   4    3
"""


# DFS Solution
#For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def mirror_image(root):
    """
    Args:
     root(BinaryTreeNode_int32)
    Returns:
     Nothing
    """
    # Write your code here.
    if root:
        root.left, root.right = root.right, root.left
        mirror_image(root.left)
        mirror_image(root.right)

# BFS Solution
from typing import *
#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

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