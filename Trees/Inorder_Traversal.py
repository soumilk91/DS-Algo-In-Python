"""
Author: Soumil Ramesh Kulkarni
Date: 01/24/2024

Question: Given a binary tree, return the inorder traversal of its node values.
"""


"""
For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
"""
def inorder(root):
    """
    Args:
     root(BinaryTreeNode_int32)
    Returns:
     list_int32
    """
    results = []

    # Define a helper Funtion for the Preorder Traversal
    def inorder_helper(root):
        # Base Case
        if root is None:
            return
        # Recursive Cases
        inorder_helper(root.left)
        results.append(root.value)
        inorder_helper(root.right)

    # Call the Helper Function
    inorder_helper(root)

    # Return the results Array
    return results