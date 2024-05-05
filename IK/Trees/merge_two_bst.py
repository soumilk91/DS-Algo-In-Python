"""
Author: Soumil Ramesh Kulkarni
Date: 02.16.2024

Question:Given two Binary Search Trees (BSTs), merge them into a single height-balanced BST.

A node with value equal to the value of the root node can be inserted either in the left or right subtree.
A binary tree is called height-balanced if for each node the following property is satisfied:
The difference in the heights of its left and right subtrees differ by at most 1.
Constraints:

1 <= number of nodes in the given BSTs <= 104
-109 <= node value <= 109
"""

#For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def inorder_traversal(root, result_list):
    if root is None:
        return result_list
    inorder_traversal(root.left, result_list)
    result_list.append((root.value, root))
    inorder_traversal(root.right, result_list)


def merge_2_sorted_lists(list1, list2):
    return_list = []
    runner1 = runner2 = 0
    while runner1 < len(list1) and runner2 < len(list2):
        if list1[runner1][0] <= list2[runner2][0]:
            return_list.append((list1[runner1][0], list1[runner1][1]))
            runner1 += 1
        else:
            return_list.append((list2[runner2][0], list2[runner2][1]))
            runner2 += 1
    while runner1 < len(list1):
        return_list.append((list1[runner1][0], list1[runner1][1]))
        runner1 += 1
    while runner2 < len(list2):
        return_list.append((list2[runner2][0], list2[runner2][1]))
        runner2 += 1
    return return_list


def create_bst_from_inorder_traversal(list1, start, end):
    if start > end:
        return None

    mid = start + (end - start) // 2
    root = list1[mid][1]

    # create Left SubTree
    root.left = create_bst_from_inorder_traversal(list1, start, mid - 1)

    # Create Right Subtree
    root.right = create_bst_from_inorder_traversal(list1, mid + 1, end)

    return root


def merge_two_binary_search_trees(root1, root2):
    """
    Args:
     root1(BinaryTreeNode_int32)
     root2(BinaryTreeNode_int32)
    Returns:
     BinaryTreeNode_int32
    """
    # Write your code here.
    inorder_root1 = []
    inorder_root2 = []

    inorder_traversal(root1, inorder_root1)
    inorder_traversal(root2, inorder_root2)

    merged_inorder = merge_2_sorted_lists(inorder_root1, inorder_root2)
    # print(merged_inorder)

    if len(merged_inorder) == 0:
        return None
    return create_bst_from_inorder_traversal(merged_inorder, 0, len(merged_inorder) - 1)



