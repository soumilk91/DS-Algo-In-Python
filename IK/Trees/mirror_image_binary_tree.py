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
