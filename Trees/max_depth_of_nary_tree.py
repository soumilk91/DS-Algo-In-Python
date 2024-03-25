"""
Author: Soumil Ramesh Kulkarni
Date: 03.24.2024

Question:
Given a n-ary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the
null value (See examples).

Example 1:
Input: root = [1,null,3,2,4,null,5,6]
Output: 3

Example 2:
Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: 5
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

from collections import deque
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        max_depth = 0
        if not root:
            return max_depth
        queue = deque([])
        queue.append((root, 1))
        while queue:
            node, current_depth = queue.popleft()
            max_depth = max(max_depth, current_depth)
            for child in node.children:
                queue.append((child, current_depth + 1))
        return max_depth

