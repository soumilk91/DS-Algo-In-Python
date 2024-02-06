# Date: 02/05/2024
# Reverse Level Order Traversal of a Binary Tree


#For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def reverse_level_order_traversal(root):
    """
    Args:
     root(BinaryTreeNode_int32)
    Returns:
     list_list_int32
    """
    # Write your code here.
    return_list = []
    queue = [root]
    while queue:
        temp_list = []
        for i in range(len(queue)):
            node = queue.pop(0)
            temp_list.append(node.value)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return_list.append(temp_list)
    return return_list[::-1]
