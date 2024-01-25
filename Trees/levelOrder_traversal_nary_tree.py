"""
Author: Soumil Ramesh Kulkarni
Date: 01/24/2024

Question: Given a tree, list node values level by level from left to right.
"""

"""
For your reference:
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []
"""


def level_order(root):
    """
    Args:
     root(TreeNode_int32)
    Returns:
     list_list_int32
    """
    results = []
    queue = []
    # Base Case for when the Tree is empty
    if root is None:
        return results

    # Traverse Logic
    queue.append(root)
    while queue:
        temp_list = []
        for i in range(len(queue)):
            node = queue.pop(0)
            temp_list.append(node.value)
            # Loop Over all the children of any given node and put them in the queue
            if node.children:
                for child in node.children:
                    queue.append(child)
        # Append the results from one level in the final list
        results.append(temp_list)

    # Return the final results list
    return results


