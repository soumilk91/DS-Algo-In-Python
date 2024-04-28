"""
Author: Soumil Ramesh Kulkarni
Date: 04.10.2024

Question:
Convert a Binary Search Tree to a sorted Circular Doubly-Linked List in place.

You can think of the left and right pointers as synonymous to the predecessor and successor pointers in a
doubly-linked list. For a circular doubly linked list, the predecessor of the first element is the last element,
and the successor of the last element is the first element.

We want to do the transformation in place. After the transformation, the left pointer of the tree node should point to
 its predecessor, and the right pointer should point to its successor. You should return the pointer to the smallest
 element of the linked list.



Example 1:
Input: root = [4,2,5,1,3]
Output: [1,2,3,4,5]

"""


# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import *
class Solution:
    def inorder(self, root, queue):
        if root is None:
            return
        self.inorder(root.left, queue)
        queue.append(root)
        self.inorder(root.right, queue)

    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        # Base Cases when there is only one node or 2 nodes in the tree
        if root is None:
            return None
        if root.left is None and root.right is None:
            root.left = root
            root.right = root
            return root

        inorder_queue = []
        self.inorder(root, inorder_queue)

        head = inorder_queue.pop(0)
        runner = head
        while len(inorder_queue) != 1:
            new_node = inorder_queue.pop(0)
            runner.right = new_node
            new_node.left = runner
            runner = runner.right

        # Since only 1 node remaining in the queue
        new_node = inorder_queue.pop(0)
        runner.right = new_node
        new_node.left = runner
        new_node.right = head
        head.left = new_node
        return head
