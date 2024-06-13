"""
Question:
Given the roots of two binary search trees, root1 and root2, return true if and only if there is a
node in the first tree and a node in the second tree whose values sum up to a given integer target.

Example 1:
Input: root1 = [2,1,4], root2 = [1,0,3], target = 5
Output: true
Explanation: 2 and 3 sum up to 5.

Example 2:
Input: root1 = [0,-10,10], root2 = [5,1,7,0,2], target = 18
Output: false

"""


# Definition for a binary tree node.
from typing import *
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def search(self, root, target):
        if not root:
            return False
        if root.val == target:
            return True
        if root.val < target:
            return self.search(root.right, target)
        else:
            return self.search(root.left, target)

    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
        if not root1 or not root2:
            return False
        from collections import deque
        queue = deque([root1])
        while queue:
            node = queue.popleft()
            searchValue = target - node.val
            if self.search(root2, searchValue):
                return True
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return False
