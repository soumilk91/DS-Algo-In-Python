"""
Author: Soumil Ramesh Kulkarni
Date: 03.09.2024

Question:
Given a binary tree, determine if it is
height-balanced
.



Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: true
Example 2:


Input: root = [1,2,2,3,3,null,null,4,4]
Output: false
Example 3:

Input: root = []
Output: true
"""

from typing import *
from collections import defaultdict
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    treeHeights = defaultdict(int)

    def height(self, node):
        if not node:
            return 0
        if node not in self.treeHeights:
            self.treeHeights[node] = 1 + max(self.height(node.left), self.height(node.right))
        returnHeight = self.treeHeights[node]
        return returnHeight

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        leftHeight = self.height(root.left)
        rightHeight = self.height(root.right)

        return (abs(leftHeight - rightHeight) < 2 and self.isBalanced(root.left) and self.isBalanced(root.right))
