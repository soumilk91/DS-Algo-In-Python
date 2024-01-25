"""
Author: Soumil Ramesh Kulkarni
Date: 01/24/2024

Question: Given a binary tree, imagine yourself standing on the right side of it and return a
          list of the node values that you can see from the top to the bottom.
"""

"""
For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
"""


def right_view(root):
    """
    Args:
     root(BinaryTreeNode_int32)
    Returns:
     list_int32
    """
    # Write your code here.

    # Use Level Order Traversal, Last Node of Each Level should be visible from the right side

    # Base Case
    return_list = []
    if root is None:
        return return_list

    queue = []
    queue.append(root)
    while queue:
        for i in range(len(queue) - 1):
            node = queue.pop(0)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        right_most_node = queue.pop(0)
        return_list.append(right_most_node.value)
        if right_most_node.left:
            queue.append(right_most_node.left)
        if right_most_node.right:
            queue.append(right_most_node.right)

    return return_list