"""
Author: Soumil Ramesh Kulkarni
Date: 03.31.2024

Question:
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.



Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 2
Example 2:

Input: root = [2,null,3,null,4,null,5,null,6]
Output: 5
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque


class Solution:
    def minDepth(self, root: TreeNode) -> int:

        visit_queue = deque([(root, 1)])

        while len(visit_queue) != 0:
            # BFS Traversal

            next_visit, cur_depth = visit_queue.popleft()

            if next_visit is None:
                # empty node or empty tree
                continue

            if next_visit.left is None and next_visit.right is None:
                # reach a leaf node
                # get the minimal depth of binary tree, early return
                return cur_depth

            # append left and right child into visit_queue, increase current depth by 1
            visit_queue.append((next_visit.left, cur_depth + 1))
            visit_queue.append((next_visit.right, cur_depth + 1))

        # depth 0 for empty-tree
        return 0