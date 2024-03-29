"""
Author: Soumil Ramesh Kulkarni
Date: 01/25/2024

Question:
Given a binary tree, check if it is a binary search tree (BST). A valid BST does not have to be complete or balanced.

Consider this definition of a BST:

All nodes values of left subtree are less than or equal to parent node value.
All nodes values of right subtree are greater than or equal to parent node value.
Both left subtree and right subtree must be BSTs.
NULL tree is a BST.
Single node trees (including leaf nodes of any tree) are BSTs.

"""

"""
For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
"""


def is_bst(root):
    """
    Args:
     root(BinaryTreeNode_int32)
    Returns:
     bool
    """
    # Write your code here.

    # Base Case for when the Tree is Empty
    if root is None:
        return True

        # Base Case from when the Tree has only one Node
    if root.left is None and root.right is None:
        return True

    # Use Level Order Traversal and check for BST Property at every traversed Node

    queue = []
    queue.append(root)
    while queue:
        node = queue.pop(0)
        if node.left and node.right:
            # Compare the values in both subtrees
            if node.value >= node.left.value and node.value <= node.right.value:
                queue.append(node.left)
                queue.append(node.right)
            else:
                return False
        elif node.left and not node.right:
            # Compare only the Left Subtree
            if node.value >= node.left.value:
                queue.append(node.left)
            else:
                return False
        elif node.right and not node.left:
            # Compare only the right Subtree
            if node.value <= node.right.value:
                queue.append(node.right)
            else:
                return False
        else:
            continue
    return True


"""
Recursive Function to check BST Property  

"""

"""
For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
"""


def is_bst_helper(root, min_value, max_value):
    # base case
    if root is None:
        return True

    if root.value < min_value or root.value > max_value:
        return False

    return is_bst_helper(root.left, min_value, root.value) and is_bst_helper(root.right, root.value, max_value)


def is_bst_recursive(root):
    """
    Args:
     root(BinaryTreeNode_int32)
    Returns:
     bool
    """
    min_value = float("-inf")
    max_value = float("inf")
    return is_bst_helper(root, min_value, max_value)
