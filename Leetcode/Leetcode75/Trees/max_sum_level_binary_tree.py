"""
Author: Soumil Ramesh Kulkarni
Date: 02.24.2024

Question:
Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.

Return the smallest level x such that the sum of all the values of nodes at level x is maximal.



Example 1:


Input: root = [1,7,0,7,-8,null,null]
Output: 2
Explanation:
Level 1 sum = 1.
Level 2 sum = 7 + 0 = 7.
Level 3 sum = 7 + -8 = -1.
So we return the level with the maximum sum which is level 2.
Example 2:

Input: root = [989,null,10250,98693,-89388,null,null,null,-32127]
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
from collections import deque

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        resultSum = -float('inf')
        resultLevel = 0
        if not root:
            return 0
        queue = deque([])
        queue.append(root)
        currLevel = 0
        while queue:
            currLevelSum = 0
            currLevel += 1
            for i in range(len(queue)):
                node = queue.popleft()
                currLevelSum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if currLevelSum > resultSum:
                resultSum = currLevelSum
                resultLevel = currLevel
        return resultLevel
