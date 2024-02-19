"""
Author: Soumil Ramesh Kulkarni
Date: 02/18/2024

Question:
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        return self.is_similar(root.left, root.right)

    def is_similar(self, leftroot, rightroot):
        # If both are none return True
        if leftroot is None and rightroot is None:
            return True

            # IF only one of them is None return False
        if leftroot is None or rightroot is None:
            return False

        # Compare the values at the Current Locations
        if leftroot.val != rightroot.val:
            return False

        # Recurse
        return self.is_similar(leftroot.left, rightroot.right) and self.is_similar(
            leftroot.right, rightroot.left
        )
