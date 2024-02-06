# Date: 02/05/2024
# Convert a binary tree into a circular Linked List



#For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def inorder_traversal(root, queue):
    if root is None:
        return
    inorder_traversal(root.left, queue)
    queue.append(root)
    inorder_traversal(root.right, queue)


def binary_tree_to_cdll(root):
    """
    Args:
     root(BinaryTreeNode_int32)
    Returns:
     BinaryTreeNode_int32
    """
    # Write your code here.
    queue = []
    inorder_traversal(root, queue)
    if len(queue) == 0:
        return None
    if len(queue) == 1:
        head = queue.pop()
        head.left = head
        head.right = head
        return head
    head = queue.pop(0)
    runner = head
    while len(queue) != 1:
        temp = queue.pop(0)
        temp.left = runner
        runner.right = temp
        runner = runner.right

    node = queue.pop(0)
    node.left = runner
    runner.right = node
    node.right = head
    head.left = node
    return head
