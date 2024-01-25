"""
Author: Soumil Ramesh Kulkarni
Date: 01/24/2024

Question: Given a binary tree, return node values in the postorder traversal order.
"""


"""
For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
"""
def postorder(root):
    """
    Args:
     root(BinaryTreeNode_int32)
    Returns:
     list_int32
    """
    results = []

    # Define a helper Funtion for the Preorder Traversal
    def postorder_helper(root):
        # Base Case
        if root is None:
            return
        # Recursive Cases
        postorder_helper(root.left)
        postorder_helper(root.right)
        results.append(root.value)

    # Call the Helper Function
    postorder_helper(root)

    # Return the results Array
    return results
