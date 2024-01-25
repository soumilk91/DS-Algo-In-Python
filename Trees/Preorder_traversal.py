"""
Author: Soumil Ramesh Kulkarni
Date: 01/24/2024

Question: Given a binary tree, return node values in the preorder traversal order.
"""

"""
For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
"""


def preorder(root):
    """
    Args:
     root(BinaryTreeNode_int32)
    Returns:
     list_int32
    """
    # Initialize an empty Array
    results = []

    # Define a helper Funtion for the Preorder Traversal
    def preorder_helper(root):
        # Base Case
        if root is None:
            return
        # Recursive Cases
        results.append(root.value)
        preorder_helper(root.left)
        preorder_helper(root.right)

    # Call the Helper Function
    preorder_helper(root)

    # Return the results Array
    return results
