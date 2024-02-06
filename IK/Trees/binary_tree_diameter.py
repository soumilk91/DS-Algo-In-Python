# Date: 02/05/2024
# Diameter of a Binary Tree
# Diameter of a binary tree is the length of the longest path between any two nodes of the tree.
# Length between any two nodes is equal to the number of edges traversed to reach one node from the other.


#For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

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
