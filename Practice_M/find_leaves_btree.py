"""
Question:
Given the root of a binary tree, collect a tree's nodes as if you were doing this:

Collect all the leaf nodes.
Remove all the leaf nodes.
Repeat until the tree is empty.


Example 1:
Input: root = [1,2,3,4,5]
Output: [[4,5,3],[2],[1]]
Explanation:
[[3,5,4],[2],[1]] and [[3,4,5],[2],[1]] are also considered correct answers since per each level it
does not matter the order on which elements are returned.

Example 2:

Input: root = [1]
Output: [[1]]
"""


# Definition for a binary tree node.
from typing import *
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        self.findLeavesHelper(root, result)
        return result

    def findLeavesHelper(self, root, result):
        if not root:
            return -1
        left = self.findLeavesHelper(root.left, result)
        right = self.findLeavesHelper(root.right, result)

        level = max(left, right) + 1

        if len(result) <= level:
            result.append([])
        result[level].append(root.val)
        return level
