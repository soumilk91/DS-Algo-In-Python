"""
Author: Soumil Ramesh Kulkarni
Date: 01/24/2024

Question: Given a linked list with elements sorted in ascending order, convert it into a height-balanced binary search tree.
"""

#For your reference:
class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def sorted_list_to_bst(head):
    """
    Args:
     head(LinkedListNode_int32)
    Returns:
     BinaryTreeNode_int32
    """
    # Write your code here.

    # Base Case of when given Linked List is Empty
    if head is None:
        return None
    sorted_list = []
    temp = head
    while temp:
        sorted_list.append(temp.value)
        temp = temp.next

    return _sorted_list_to_bst_helper(sorted_list, 0, len(sorted_list) - 1)


def _sorted_list_to_bst_helper(sorted_list, start, end):
    # Base Case
    if start > end:
        return None

    mid = (start + end) // 2
    root = BinaryTreeNode(sorted_list[mid])

    # Create Left and Right Subtrees
    root.left = _sorted_list_to_bst_helper(sorted_list, start, mid - 1)

    root.right = _sorted_list_to_bst_helper(sorted_list, mid + 1, end)

    return root
