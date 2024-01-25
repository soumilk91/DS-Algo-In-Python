"""
Author: Soumil Ramesh Kulkarni
Date: 01/24/2024

Question: Given a binary tree, return the bottom-up level order traversal of the node values listing each level from left to right.
"""


"""
For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
"""
def reverse_level_order_traversal(root):
    """
    Args:
     root(BinaryTreeNode_int32)
    Returns:
     list_list_int32
    """
    # Initialize an empty Array used for Storing the Final Results
    results = []

    # Initialize a Queue
    queue = []

    # Base Case for when the Tree is Empty
    if root is None:
        return results

    queue.append(root)
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
        # Append the temp_list containing values from one level in the final results list
        results.append(temp_list)

    # Return the final results list
    return results[::-1]
