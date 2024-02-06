# Date: 02/05/2024
# Print all Paths of a tree from root node to leaf Node


#For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def all_paths_of_a_binary_tree(root):
    """
    Args:
     root(BinaryTreeNode_int32)
    Returns:
     list_list_int32
    """
    # Write your code here.
    if root is None:
        return []
    return_list = []
    # We User Preorder Traversal
    _helper(root, [], return_list)
    return return_list


def _helper(root, slate, return_list):
    # Base Case
    if root is None:
        return

    # When we reach the Leaf Node
    if root.left is None and root.right is None:
        slate.append(root.value)
        return_list.append(slate[:])
        slate.pop()
        return

    # Append the current node value to the temp slate
    slate.append(root.value)

    if root.left:
        _helper(root.left, slate, return_list)

    if root.right:
        _helper(root.right, slate, return_list)

    slate.pop()


