"""
Author: Soumil Ramesh Kulkarni
Date: 02.24.2024

Question:
Given a root node reference of a BST and a key, delete the node with the given key in the BST.
Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:

Search for a node to remove.
If the node is found, delete the node.


Example 1:


Input: root = [5,3,6,2,4,null,7], key = 3
Output: [5,4,6,2,null,null,7]
Explanation: Given key to delete is 3. So we find the node with value 3 and delete it.
One valid answer is [5,4,6,2,null,null,7], shown in the above BST.
Please notice that another valid answer is [5,2,6,null,4,null,7] and it's also accepted.

Example 2:

Input: root = [5,3,6,2,4,null,7], key = 0
Output: [5,3,6,2,4,null,7]
Explanation: The tree does not contain a node with value = 0.
Example 3:

Input: root = [], key = 0
Output: []
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        if root.val > key:
            # Target node is smaller than current node, search left
            root.left = self.deleteNode(root.left, key)

        elif root.val < key:
            # target node is larger than current node, search right
            root.right = self.deleteNode(root.right, key)

        else:
            # Current node is Target Node

            if not root.left or not root.right:
                # If one child is empty
                # Target Node is replaced by the non-empty child
                if root.left:
                    root = root.left
                else:
                    root = root.right

            else:
                # Both Children exist
                # Target Node is replaced by smallest element in right Subtree
                curr = root.right
                while curr.left:
                    curr = curr.left

                root.val = curr.val
                root.right = self.deleteNode(root.right, curr.val)
        return root