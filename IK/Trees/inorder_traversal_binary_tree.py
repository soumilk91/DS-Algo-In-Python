# Date: 02/05/2024
# Inorder Traversal of Binary Tree



#For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None



def inorder(root):
    """
    Args:
     root(BinaryTreeNode_int32)
    Returns:
     list_int32
    """
    # Write your code here.
    return_list = []
    inorder_helper(root, return_list)
    return return_list


def inorder_helper(root, return_list):
    # Base Case
    if root is None:
        return

    # Recurse
    inorder_helper(root.left, return_list)
    return_list.append(root.value)
    inorder_helper(root.right, return_list)
