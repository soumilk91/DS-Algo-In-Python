"""
Author: Soumil Ramesh Kulkarni
Date: 02.18.2024

Question:
Given the root of a Binary Search Tree (BST), return the minimum absolute difference between the values of
any two different nodes in the tree.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorder_traversal(self, root, result_list):
        if root is None:
            return
        self.inorder_traversal(root.left, result_list)
        result_list.append(root.val)
        self.inorder_traversal(root.right, result_list)

    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        sorted_list = []
        self.inorder_traversal(root, sorted_list)
        min_diff = float('inf')

        runner = 0
        while runner < len(sorted_list) - 1:
            temp = sorted_list[runner + 1] - sorted_list[runner]
            if temp < min_diff:
                min_diff = temp
            runner += 1
        return min_diff
