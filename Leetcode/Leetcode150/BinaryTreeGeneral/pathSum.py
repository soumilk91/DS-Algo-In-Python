"""
Author: Soumil ramesh Kulkarni
Date: 02/18/2024

Question: Given the root of a binary tree and an integer targetSum,
return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # Base Case for when the Tree is Empty
        if root is None:
            return False
        # We use BFS
        queue = []
        queue.append((root, targetSum))
        while queue:
            node = queue.pop(0)

            # check if leaf node and targetSum is 0
            if node[0].left is None and node[0].right is None:
                if node[1] - node[0].val == 0:
                    return True

            # If left and right Subtrees Present, insert into the queue
            # Reduce the targetSum from the set appended to the queue
            if node[0].left:
                queue.append((node[0].left, node[1] - node[0].val))

            if node[0].right:
                queue.append((node[0].right, node[1] - node[0].val))

        # Return False if none of the Path Sums add up to the targetSum
        return False

