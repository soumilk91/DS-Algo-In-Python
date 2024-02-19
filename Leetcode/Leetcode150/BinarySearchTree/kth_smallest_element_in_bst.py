"""
Author: Soumil Ramesh Kulkarni
Date: 02.18.2024

Question:
Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of
all the values of the nodes in the tree.

Input: root = [3,1,4,null,2], k = 1
Output: 1
Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorder_traversal(self, root, k, result):
        if root is None:
            return result
        if len(result) == k:
            return result
        self.inorder_traversal(root.left, k, result)
        result.append(root.val)
        self.inorder_traversal(root.right, k, result)

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        result = []
        self.inorder_traversal(root, k, result)
        print(result)
        return result[k - 1]

