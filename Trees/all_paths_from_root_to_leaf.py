"""
Author: Soumil Ramesh Kulkarni
Date: 01/25/2024

Question:

Given a binary tree, return all paths from root to leaf.

"""

"""
For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
"""


def all_paths_of_a_binary_tree(root):
    """
    Args:
     root(BinaryTreeNode_int32)
    Returns:
     list_list_int32
    """
    # Write your code here.
    if root is None:
        return []
    return_list = []
    # We User Preorder Traversal
    _helper(root, [], return_list)
    return return_list


def _helper(root, slate, return_list):
    # Base Case
    if root is None:
        return

    # When we reach the Leaf Node
    if root.left is None and root.right is None:
        slate.append(root.value)
        return_list.append(slate[:])
        slate.pop()
        return

    # Append the current node value to the temp slate
    slate.append(root.value)

    if root.left:
        _helper(root.left, slate, return_list)

    if root.right:
        _helper(root.right, slate, return_list)

    slate.pop()


###################   Iterative Solution ######################

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque
from typing import *
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []
        result = []

        queue = deque([(root, "")])
        while queue:
            node, currentPath = queue.popleft()
            currentPath += str(node.val)
            if node.left is None and node.right is None:
                result.append(currentPath)
            if node.left:
                queue.append((node.left, currentPath + "->"))
            if node.right:
                queue.append((node.right, currentPath + "->"))
        return result