# Date: 02/05/2024
# Find the LCA of two given nodes from the binary Tree
"""
Approach:

Follow the steps to implement the above approach:

-> Create a hash table or a map to store the parent pointers of each node in the binary tree.
-> Traverse the binary tree and populate the hash table or the map with the parent pointers for each node.
-> Starting from the first node, traverse up the tree and add each ancestor to a set or a list.
-> Starting from the second node, traverse up the tree and check if each ancestor is already in the set or the list.
    The first ancestor that is already in the set or the list is the lowest common ancestor.
-> If no common ancestor is found, return null or any other value that indicates the absence of a common ancestor.
"""

"""
For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
"""


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        p_val = p.val
        q_val = q.val

        node = root

        while node:
            parent_val = node.val

            if p_val > parent_val and q_val > parent_val:
                node = node.right
            elif p_val < parent_val and q_val < parent_val:
                node = node.left
            else:
                return node