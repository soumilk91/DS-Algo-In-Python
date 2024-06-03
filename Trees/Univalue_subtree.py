"""
Author: Soumil Ramesh Kulkarni
Date: 01/25/2024

Question: Given a binary tree, find the number of unival subtrees.
          An unival (single value) tree is a tree that has the same value in every node.
"""

"""
For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
"""


def find_single_value_trees(root):
    """
    Args:
     root(BinaryTreeNode_int32)
    Returns:
     int32
    """
    # Write your code here.
    compare_is_univalue = {}
    return_number = [0]
    _helper(root, return_number, compare_is_univalue)
    return return_number[0]


def _helper(root, return_number, compare_is_univalue):
    # Base Case for when the Tree is Empty
    if root is None:
        return

    # Base Case for when we have reached the leaf Node. All Leaf Nodes by default are univalue subtrees
    if root.left is None and root.right is None:
        compare_is_univalue[root] = True
        return_number[0] += 1
        return

    # Post Order Traversal
    _helper(root.left, return_number, compare_is_univalue)
    _helper(root.right, return_number, compare_is_univalue)

    # Process
    # At Each Node if node.value == node.left.value == node.right.value and node.left is univalue and node.right
    # is univalue then the current node is univalue

    # Node has both left and right Child
    if root.left and root.right:
        if root.value == root.left.value == root.right.value and compare_is_univalue[root.left] and compare_is_univalue[
            root.right]:
            compare_is_univalue[root] = True
            return_number[0] += 1
        else:
            compare_is_univalue[root] = False
    # Node only has Left Subtree
    elif root.left and not root.right:
        if root.value == root.left.value and compare_is_univalue[root.left]:
            compare_is_univalue[root] = True
            return_number[0] += 1
        else:
            compare_is_univalue[root] = False
    # Node only has Right Subtree
    else:
        if root.value == root.right.value and compare_is_univalue[root.right]:
            compare_is_univalue[root] = True
            return_number[0] += 1
        else:
            compare_is_univalue[root] = False