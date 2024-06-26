"""
Author: Soumil Ramesh Kulkarni
Date: 01/24/2024

Question: Given a binary tree and an integer k, check whether the tree has a root to leaf path with a sum of values equal to k.
"""



#For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
def path_sum(root, k):
    """
    Args:
     root(BinaryTreeNode_int32)
     k(int32)
    Returns:
     bool
    """
    # Write your code here.
    # Again We will be Using Level Order Traversal

    if root is None:
        return False

    compare_dict = {}
    queue = []
    queue.append(root)
    compare_dict[root] = root.value

    while queue:
        node = queue.pop(0)

        if node.left is None and node.right is None:
            if compare_dict[node] == k:
                return True

        if node.left:
            compare_dict[node.left] = compare_dict[node] + node.left.value
            queue.append(node.left)

        if node.right:
            compare_dict[node.right] = compare_dict[node] + node.right.value
            queue.append(node.right)
    return False


####################### Recursive Solution ######################

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import *
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        targetSum -= root.val
        if not root.left and not root.right:
            return targetSum == 0

        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)
