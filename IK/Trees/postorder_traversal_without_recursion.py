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
    # -> Keep a Track of visited Nodes in dict
    # Write your code here.
    return_list = []
    visited_dict = {}
    runner = root
    while runner and runner not in visited_dict:
        if runner.left and runner.left not in visited_dict:
            runner = runner.left
        elif runner.right and runner.right not in visited_dict:
            runner = runner.right
        else:
            visited_dict[runner] = True
            return_list.append(runner.value)
            runner = root
    return return_list