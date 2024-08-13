# Date: 02/05/2024
# Diameter of a Binary Tree
# Diameter of a binary tree is the length of the longest path between any two nodes of the tree.
# Length between any two nodes is equal to the number of edges traversed to reach one node from the other.


#For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

from typing import *
class Solution:
    def diameterOfBinaryTree(self, root: Optional[BinaryTreeNode]) -> int:
        diameter = 0

        def longestPath(node):
            if not node:
                return 0
            nonlocal diameter
            leftPath = longestPath(node.left)
            rightPath = longestPath(node.right)

            diameter = max(diameter, leftPath + rightPath)

            return 1 + max(leftPath, rightPath)

        longestPath(root)
        return diameter