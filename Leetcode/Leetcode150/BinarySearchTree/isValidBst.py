"""
Author: Soumil Ramesh Kulkarni
Date: 02.15.2024

Question:
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left
subtree
 of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.


"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST_helper(self, root, minimum, maximum):
        # Base Case
        if root is None:
            return True

            # Compare the node Values
        if root.val < minimum:
            return False
        if root.val > maximum:
            return False
        # Recurse in both subtrees
        return self.isValidBST_helper(root.left, minimum, root.val - 1) and self.isValidBST_helper(root.right,
                                                                                                   root.val + 1,
                                                                                                   maximum)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return False
        return self.isValidBST_helper(root, -float('inf'), float('inf'))
