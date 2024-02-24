"""
Author: Soumil Ramesh Kulkarni
Date: 02.24.2024

Question:
Given a binary tree, find the largest subtree that's a binary search tree (BST).

Here the largest subtree means a subtree with maximum number of nodes.

Example
Example one

Output:

3
There are seven distinct subtrees. Five of them are BSTs
(rooted in 300, 200, 400, 600, 700). Sizes if those five are 3, 1, 1, 1 and 1 respectively.
The largest BST subtree has 3 nodes.
"""


"""
* Asymptotic complexity in terms of total number of nodes in the given tree `n`:
* Time: O(n).
* Auxiliary space: O(n).
* Total space: O(n).
"""
# Class to store BST information of a tree
class BSTInfo:
    def __init__(self):
        self.mn = float('-inf')   # default minimum as the node value can be -10^9 minimum
        self.mx = float('inf')    # default maximum as the node value can be 10^9 max
        self.isBST = True         # an empty tree is a BST by definition
        self.size = 0             # size of an empty bst is 0
        self.mxSize = 0           # maximum size of the empty bst is 0

def helper(root):
    current_tree_info = BSTInfo()
    if root is None:
        # Base case: If the current tree is None, return as an empty BST.
        return current_tree_info

    # Leaf node check
    if root.left is None and root.right is None:
        current_tree_info.mn = root.value
        current_tree_info.mx = root.value
        current_tree_info.size = 1
        current_tree_info.isBST = True
        current_tree_info.mxSize = 1
    elif root.left is None:
        right_tree_info = helper(root.right)
        if right_tree_info.isBST and root.value <= right_tree_info.mn:
            current_tree_info.mn = root.value
            current_tree_info.mx = right_tree_info.mx
            current_tree_info.size = 1 + right_tree_info.size
            current_tree_info.isBST = True
            current_tree_info.mxSize = max(current_tree_info.size, right_tree_info.mxSize)
        else:
            current_tree_info.isBST = False
            current_tree_info.mxSize = right_tree_info.mxSize
    elif root.right is None:
        left_tree_info = helper(root.left)
        if left_tree_info.isBST and left_tree_info.mx <= root.value:
            current_tree_info.mn = left_tree_info.mn
            current_tree_info.mx = root.value
            current_tree_info.size = 1 + left_tree_info.size
            current_tree_info.isBST = True
            current_tree_info.mxSize = max(current_tree_info.size, left_tree_info.mxSize)
        else:
            current_tree_info.isBST = False
            current_tree_info.mxSize = left_tree_info.mxSize
    else:
        left_tree_info = helper(root.left)
        right_tree_info = helper(root.right)
        if left_tree_info.isBST and right_tree_info.isBST and left_tree_info.mx <= root.value <= right_tree_info.mn:
            # If both subtrees are BST and current root value is greater than or equal to the maximum value of left subtree
            # and less than or equal to right subtree.
            current_tree_info.mn = left_tree_info.mn
            current_tree_info.mx = right_tree_info.mx
            current_tree_info.size = 1 + left_tree_info.size + right_tree_info.size
            current_tree_info.isBST = True
            current_tree_info.mxSize = max(current_tree_info.size, max(left_tree_info.mxSize, right_tree_info.mxSize))
        else:
            current_tree_info.isBST = False
            current_tree_info.mxSize = max(left_tree_info.mxSize, right_tree_info.mxSize)
    return current_tree_info

def find_largest_bst(root):
    if root is None:
        return 0
    result = helper(root)
    return result.mxSize