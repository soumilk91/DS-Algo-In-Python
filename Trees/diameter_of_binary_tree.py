"""
Author: Soumil Ramesh Kulkarni
Date: 01/24/2024

Question: Given a binary tree, find its diameter.

"""

"""
For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
"""


def binary_tree_diameter(root):
    """
    Args:
     root(BinaryTreeNode_int32)
    Returns:
     int32
    """
    # Write your code here.
    if root is None:
        return 0
    result = [0]
    _binary_tree_helper(root, result)
    return result[0]


def _binary_tree_helper(root, result):
    if root is None:
        return 0

    left_subtree_height = _binary_tree_helper(root.left, result)
    right_subtree_height = _binary_tree_helper(root.right, result)

    result[0] = max(result[0], left_subtree_height + right_subtree_height)

    return 1 + max(left_subtree_height, right_subtree_height)
