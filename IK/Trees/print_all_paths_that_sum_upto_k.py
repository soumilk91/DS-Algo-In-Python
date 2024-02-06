# Date: 02/05/2024
# Given a binary tree and an integer k, find all the root to leaf paths that sum to k.


#For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def all_paths_sum_k(root, k):
    """
    Args:
     root(BinaryTreeNode_int32)
     k(int32)
    Returns:
     list_list_int32
    """
    # Write your code here.
    result_list = []

    # Base Case for when the Given Tree is Empty
    if root is None:
        return result_list

    all_path_sum_k(root, k, [], result_list)
    if not result_list:
        result_list.append([-1])
    return result_list


def all_path_sum_k(root, k, slate, result_list):
    # PreOrder Traversal Bottom Up Approach

    slate.append(root.value)
    k -= root.value

    # When we reach the Leaf Node
    if root.left is None and root.right is None:
        if k == 0:
            result_list.append(slate[:])
        slate.pop()
        return

    # Left Subtree
    if root.left:
        all_path_sum_k(root.left, k, slate, result_list)

    # Right Subtree
    if root.right:
        all_path_sum_k(root.right, k, slate, result_list)

    slate.pop()