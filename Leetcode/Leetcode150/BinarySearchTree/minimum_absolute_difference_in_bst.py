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

from typing import *
class Solution:
    def inorder(self, root, sortedList, result):
        if not root:
            return

        self.inorder(root.left, sortedList, result)
        sortedList.append(root.val)
        if len(sortedList) > 1:
            result[0] = min(result[0], (sortedList[-1] - sortedList[-2]))
            print(result[0])
        self.inorder(root.right, sortedList, result)

    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        sortedList = []
        result = [float("inf")]
        self.inorder(root, sortedList, result)
        return result[0]
