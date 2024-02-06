# Date: 02.05.2024
# Clone a given Binary Tree and return the root node of the n=cloned Tree


#For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def clone_tree(root):
    """
    Args:
     root(BinaryTreeNode_int32)
    Returns:
     BinaryTreeNode_int32
    """
    # Write your code here.

    # Base Case
    if root is None:
        return root

    clone_root = BinaryTreeNode(root.value)

    clone_root.left = clone_tree(root.left)
    clone_root.right = clone_tree(root.right)

    return clone_root

