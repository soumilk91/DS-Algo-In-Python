"""
Author: Soumil Ramesh Kulkarni
Date: 02.24.2024

Question:

"""


#For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.next_right = None


from queue import Queue


def populate_sibling_pointers(root):
    """
    Args:
     root(BinaryTreeNode_int32)
    Returns:
     BinaryTreeNode_int32
    """
    # Write your code here.
    # Use BFS

    if root is None:
        return None
    queue = Queue()
    queue.put(root)
    while not queue.empty():
        queue_size = queue.qsize()
        prev = None
        for i in range(queue_size):
            current_node = queue.get()

            if prev is not None:
                prev.next_right = current_node
            if current_node.left:
                queue.put(current_node.left)
            if current_node.right:
                queue.put(current_node.right)
            prev = current_node
    return root