"""
Author: Soumil Ramesh Kulkarni
Date: 02.18.2024

Question:
Given the root of a binary tree, flatten the tree into a "linked list":

The "linked list" should use the same TreeNode class where the right child pointer points
 to the next node in the list and the left child pointer is always null.
The "linked list" should be in the same order as a pre-order traversal of the binary tree.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None:
            return

        stack = []
        queue = []
        stack.append(root)
        while stack:
            node = stack.pop()
            queue.append(node)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        root = queue.pop(0)
        root.left = None
        runner = root
        for i in queue:
            runner.right = i
            runner = runner.right
            runner.left = None


