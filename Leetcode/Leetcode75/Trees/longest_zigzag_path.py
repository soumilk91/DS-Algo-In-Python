"""
Author: Soumil Ramesh Kulkarni
Date: 02.24.2024

Question:
You are given the root of a binary tree.

A ZigZag path for a binary tree is defined as follow:

Choose any node in the binary tree and a direction (right or left).
If the current direction is right, move to the right child of the current node; otherwise, move to the left child.
Change the direction from right to left or from left to right.
Repeat the second and third steps until you can't move in the tree.
Zigzag length is defined as the number of nodes visited - 1. (A single node has a length of 0).

Return the longest ZigZag path contained in that tree.
Input: root = [1,null,1,1,1,null,null,1,1,null,1,null,null,null,1]
Output: 3
Explanation: Longest ZigZag path in blue nodes (right -> left -> right).

Input: root = [1,1,1,null,1,null,null,1,1,null,1]
Output: 4
Explanation: Longest ZigZag path in blue nodes (left -> right -> left -> right).
Example 3:

Input: root = [1]
Output: 0
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = []
        max_zigzag_size = 0
        if root.left:
            queue.append((root.left, 'l', 1))
        if root.right:
            queue.append((root.right, 'r', 1))
        while queue:
            node, _from, zigzag_size = queue.pop(0)
            max_zigzag_size = max(max_zigzag_size, zigzag_size)
            if node.left:
                if _from == 'l':
                    queue.append((node.left, 'l', 1))
                if _from == 'r':
                    queue.append((node.left, 'l', zigzag_size + 1))
            if node.right:
                if _from == 'l':
                    queue.append((node.right, 'r', zigzag_size + 1))
                if _from == 'r':
                    queue.append((node.right, 'r', 1))
        return max_zigzag_size
