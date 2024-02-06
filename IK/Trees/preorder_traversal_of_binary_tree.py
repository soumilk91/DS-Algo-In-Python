# Date: 02/05/2024
# Preorder Traversal of Binary Tree



#For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def preorder(root):
    """
    Args:
     root(BinaryTreeNode_int32)
    Returns:
     list_int32
    """
    # Write your code here.
    return_list = []
    preorder_helper(root, return_list)
    return return_list

def preorder_helper(root, return_list):
    # Base Case
    if root is None:
        return

    # recurse
    return_list.append(root.value)
    preorder_helper(root.left, return_list)
    preorder_helper(root.right, return_list)
