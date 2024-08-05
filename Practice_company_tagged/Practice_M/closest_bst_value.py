"""
Author: Soumil Ramesh Kulkarni
Date: 03.21.2024

Question:
Given the root of a binary search tree and a target value, return the value in the BST that is closest to the target. If there are multiple answers, print the smallest.

Example 1:
Input: root = [4,2,5,1,3], target = 3.714286
Output: 4

Example 2:
Input: root = [1], target = 4.428571
Output: 1
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        c = root.val if root else None
        while root:
            if abs(root.val - target) < abs(c - target):
                c = root.val
            elif abs(root.val - target) == abs(c - target):
                c = min(root.val, c)
            if root.val < target:
                root = root.right
            else:
                root = root.left
        return c