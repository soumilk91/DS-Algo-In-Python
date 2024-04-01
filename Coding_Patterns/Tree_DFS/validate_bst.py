"""
Author: Soumil Ramesh Kulkarni
Date: 03.31.2024

Question:
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left
subtree
 of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.


Example 1:


Input: root = [2,1,3]
Output: true
Example 2:


Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST_helper(self, node, minimum, maximum):
        if node is None:
            return True
        if node.val < minimum:
            return False
        if node.val > maximum:
            return False
        return self.isValidBST_helper(node.left, minimum, node.val - 1) and self.isValidBST_helper(node.right,
                                                                                                   node.val + 1,
                                                                                                   maximum)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        return self.isValidBST_helper(root, float("-inf"), float("inf"))
