"""
Author: Soumil Ramesh Kulkarni
Date: 04.03.2024

Question:
Given the root of a binary tree, return the number of nodes where the value of the node is equal to the
average of the values in its subtree.

Note:

The average of n elements is the sum of the n elements divided by n and rounded down to the nearest integer.
A subtree of root is a tree consisting of root and all of its descendants.


Example 1:


Input: root = [4,8,5,0,1,null,6]
Output: 5
Explanation:
For the node with value 4: The average of its subtree is (4 + 8 + 5 + 0 + 1 + 6) / 6 = 24 / 6 = 4.
For the node with value 5: The average of its subtree is (5 + 6) / 2 = 11 / 2 = 5.
For the node with value 0: The average of its subtree is 0 / 1 = 0.
For the node with value 1: The average of its subtree is 1 / 1 = 1.
For the node with value 6: The average of its subtree is 6 / 1 = 6.
Example 2:


Input: root = [1]
Output: 1
Explanation: For the node with value 1: The average of its subtree is 1 / 1 = 1.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.return_nodes = 0

    def averageOfSubtree_helper(self, node):
        if node is None:
            return 0, 0  # Sum and Number of Nodes

        leftSubtree = self.averageOfSubtree_helper(node.left)
        rightSubtree = self.averageOfSubtree_helper(node.right)

        # Calculate
        sumofValues = leftSubtree[0] + rightSubtree[0] + node.val
        numberofNodes = leftSubtree[1] + rightSubtree[1] + 1

        # Check if the current Node's value == average of its subtree
        if sumofValues // numberofNodes == node.val:
            self.return_nodes += 1

        return sumofValues, numberofNodes

    def averageOfSubtree(self, root: TreeNode) -> int:
        self.averageOfSubtree_helper(root)
        return self.return_nodes