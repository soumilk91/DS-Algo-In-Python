"""
Author: Soumil Ramesh Kulkarni
Date: 02.24.2024

Question:
Given inorder and preorder traversal of a valid binary tree, you have to construct the binary tree.

Example One
{
"inorder": [2, 1, 3],
"preorder": [1, 2, 3]
}
Output:

  1
 / \
2   3
Example Two
{
"inorder": [3, 2, 1, 5, 4, 6],
"preorder": [1, 2, 3, 4, 5, 6]
}
Output:

   1
  /  \
 2    4
/    /  \
3    5   6
"""



#For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def construct_binary_tree(inorder, preorder):
    """
    Args:
     inorder(list_int32)
     preorder(list_int32)
    Returns:
     BinaryTreeNode_int32
    """
    # Write your code here.
    def array_to_tree(left, right):
            nonlocal preorder_index
            # if there are no elements to construct the tree
            if left > right: return None

            # select the preorder_index element as the root and increment it
            root_value = preorder[preorder_index]
            root = BinaryTreeNode(root_value)


            preorder_index += 1

            # build left and right subtree
            # excluding inorder_index_map[root_value] element because it's the root
            root.left = array_to_tree(left, inorder_index_map[root_value] - 1)
            root.right = array_to_tree(inorder_index_map[root_value] + 1, right)

            return root


    preorder_index = 0
    # build a hashmap to store value -> its index relations
    inorder_index_map = {}
    for index, value in enumerate(inorder):
        inorder_index_map[value] = index

    return array_to_tree(0, len(preorder) - 1)