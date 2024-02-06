# Date: 02/05/2024
# Postorder Traversal of Binary Tree



#For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def postorder(root):
    """
    Args:
     root(BinaryTreeNode_int32)
    Returns:
     list_int32
    """
    # Write your code here.
    return_list = []
    postorder_helper(root, return_list)
    return return_list


def postorder_helper(root, return_list):
    # Base Case
    if root is None:
        return

        # Recurse
    postorder_helper(root.left, return_list)
    postorder_helper(root.right, return_list)
    return_list.append(root.value)
