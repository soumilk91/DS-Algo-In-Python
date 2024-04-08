"""
Author: Soumil Ramesh Kulkarni
Date: 01/28/2024

Question:
Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a leaf value sequence.
For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).

Two binary trees are considered leaf-similar if their leaf value sequence is the same.

Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.

Eg:
Input: root1 = [3,5,1,6,2,9,8,null,null,7,4], root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
Output: true

Input: root1 = [1,2,3], root2 = [1,3,2]
Output: false

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def dfs_preorder(self, root, return_list):
        if root is None:
            return
        if root.left is None and root.right is None:
            return_list.append(root.val)
        self.dfs_preorder(root.left, return_list)
        self.dfs_preorder(root.right, return_list)

    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        # We will do a Preorder DFS traversal on both trees and only record the leaf nodes in a list and compare the 2 lists
        # We cannot do a BFS because the order of the leaves is important 

        tree1_leaf_nodes = []
        self.dfs_preorder(root1, tree1_leaf_nodes)
        tree2_leaf_nodes = []
        self.dfs_preorder(root2, tree2_leaf_nodes)
        return tree1_leaf_nodes == tree2_leaf_nodes
