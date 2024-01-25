"""
Author: Soumil Ramesh Kulkarni
Date: 01/24/2024

Question: Given a binary tree, return the zigzag level order traversal of the node values
          listing the odd levels from left to right and the even levels from right to left.
"""

"""
For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
"""

"""
For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
"""


def zigzag_level_order_traversal(root):
    """
    Args:
     root(BinaryTreeNode_int32)
    Returns:
     list_list_int32
    """
    # Write your code here.
    # Always Use Iterative Approach for Level Order Traversals

    # Initialize an empty Array used for Storing the Final Results
    results = []

    # Initialize a Queue
    queue = []

    # Base Case for when the Tree is Empty
    if root is None:
        return results

    queue.append(root)

    level_number = 1

    # Always have a for Loop inside the While Loop. For Loop length would be the length of the Queue
    while queue:
        # Initialize a temp list to store values at one particular level
        temp_list = []
        for i in range(len(queue)):
            # Pop Elements from the queue
            node = queue.pop(0)
            temp_list.append(node.value)

            # Queue the node if it has left child and if it has right child
            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

        # If level_number is even, reverse temp_list
        if level_number % 2 == 0:
            temp_list = temp_list[::-1]

        # Increment level_number by 1
        level_number += 1

        # Append the temp_list containing values from one level in the final results list
        results.append(temp_list)

    # Return the final results list
    return results
