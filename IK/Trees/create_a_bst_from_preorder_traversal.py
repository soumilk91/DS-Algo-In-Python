"""
Author: Soumil Ramesh Kulkarni
Date: 02.15.2924

Question: Construct A Binary Search Tree From Its Preorder Traversal
Construct a Binary Search Tree whose preorder traversal matches the given list.

"""

#For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def build_binary_search_tree(preorder):
    """
    Args:
     preorder(list_int32)
    Returns:
     BinaryTreeNode_int32
    """
    # Write your code here.
    if not preorder:
        return None

    root = BinaryTreeNode(preorder[0])

    def insert_node(value, node):
        while True:
            if value <= node.value:
                if node.left:
                    node = node.left
                else:
                    node.left = BinaryTreeNode(value)
                    break
            else:
                if node.right:
                    node = node.right
                else:
                    node.right = BinaryTreeNode(value)
                    break

    runner = root
    for i in range(1, len(preorder)):
        runner = root
        insert_node(preorder[i], runner)
    return root
