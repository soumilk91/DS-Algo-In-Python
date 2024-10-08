"""
Author: Soumil Ramesh Kulkarni
Date: 03.09.2024

Question:
You are given the root of a binary tree containing digits from 0 to 9 only.

Each root-to-leaf path in the tree represents a number.

For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.
Return the total sum of all root-to-leaf numbers. Test cases are generated so that the answer will fit in a 32-bit integer.

A leaf node is a node with no children.



Example 1:


Input: root = [1,2,3]
Output: 25
Explanation:
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.
Therefore, sum = 12 + 13 = 25.
Example 2:


Input: root = [4,9,0,5,1]
Output: 1026
Explanation:
The root-to-leaf path 4->9->5 represents the number 495.
The root-to-leaf path 4->9->1 represents the number 491.
The root-to-leaf path 4->0 represents the number 40.
Therefore, sum = 495 + 491 + 40 = 1026.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import *
from collections import deque


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        result = 0
        if not root:
            return result
        queue = deque([])
        queue.append((root, 0))
        while queue:
            node, number = queue.popleft()
            number = (number * 10) + node.val
            if not node.left and not node.right:
                result += number
            if node.left:
                queue.append((node.left, number))
            if node.right:
                queue.append((node.right, number))
        return result
