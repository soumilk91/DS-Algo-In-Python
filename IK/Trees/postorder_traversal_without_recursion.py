# Date: 02/05/2024
# Postorder Treversal on a Binary Tree without Recursion



#For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def postorder_traversal(root):
    """
    Args:
     root(BinaryTreeNode_int32)
    Returns:
     list_int32
    """
    # Write your code here.
    postorder = []
    if not root:
        return postorder

    stack = [root]
    while stack:
        current_node = stack.pop()
        postorder.append(current_node.value)

        if current_node.left:
            stack.append(current_node.left)
        if current_node.right:
            stack.append(current_node.right)
    return postorder[::-1]
