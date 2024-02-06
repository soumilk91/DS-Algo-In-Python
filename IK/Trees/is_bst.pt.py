# Date: 02/05/2024
# Is a Given Binary Tree, BST ?



#For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def is_bst_helper(root, min_value, max_value):
    # base case
    if root is None:
        return True

    if root.value < min_value or root.value > max_value:
        return False

    return is_bst_helper(root.left, min_value, root.value) and is_bst_helper(root.right, root.value, max_value)


def is_bst(root):
    """
    Args:
     root(BinaryTreeNode_int32)
    Returns:
     bool
    """
    min_value = float("-inf")
    max_value = float("inf")
    return is_bst_helper(root, min_value, max_value)
