"""
Author: Soumil Ramesh Kulkarni
Date: 01/28/2024

Question:
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

EG:
Input: root = [3,9,20,null,null,15,7]
Output: 3

Input: root = [1,null,2]
Output: 2

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque
from typing import *


class Solution1:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = deque([])
        maxDepthfound = 0
        queue.append((root, 1))
        while queue:
            node, currDepth = queue.popleft()
            maxDepthfound = max(maxDepthfound, currDepth)
            if node.left:
                queue.append((node.left, currDepth + 1))
            if node.right:
                queue.append((node.right, currDepth + 1))
        return maxDepthfound


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))




