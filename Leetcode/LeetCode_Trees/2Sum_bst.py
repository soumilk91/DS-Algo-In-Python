"""
Author: Soumil Ramesh Kulkarni
Date: 04.14.2024

Question:
Given the root of a binary search tree and an integer k, return true if there exist two elements
in the BST such that their sum is equal to k, or false otherwise.

Example 1:
Input: root = [5,3,6,2,4,null,7], k = 9
Output: true

Example 2:
Input: root = [5,3,6,2,4,null,7], k = 28
Output: false
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import deque
from typing import *

class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        hashtable = {}
        queue = deque([])
        queue.append(root)
        while queue:
            node = queue.popleft()
            if k - node.val in hashtable:
                return True
            if node.val not in hashtable:
                hashtable[node.val] = 1
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return False


class Solution1:
    def inorder_traversal(self, root, result):
        if not root:
            return
        self.inorder_traversal(root.left, result)
        result.append(root.val)
        self.inorder_traversal(root.right, result)

    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        result = []
        self.inorder_traversal(root, result)
        start = 0
        end = len(result) - 1

        while start < end:
            temp_sum = result[start] + result[end]
            if temp_sum == k:
                return True
            elif temp_sum < k:
                start += 1
            else:
                end -= 1
        return False
