"""
Author: Soumil Ramesh Kulkarni
Date: 04.10.2024

Question:
You are given a doubly linked list, which contains nodes that have a next pointer, a previous pointer,
and an additional child pointer. This child pointer may or may not point to a separate doubly linked list,
also containing these special nodes. These child lists may have one or more children of their own, and so on,
to produce a multilevel data structure as shown in the example below.

Given the head of the first level of the list, flatten the list so that all the nodes appear in a single-level,
doubly linked list. Let curr be a node with a child list. The nodes in the child list should appear after curr
and before curr.next in the flattened list.

Return the head of the flattened list. The nodes in the list must have all of their child pointers set to null.
Input: head = [1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]
Output: [1,2,3,7,8,11,12,9,10,4,5,6]
Explanation: The multilevel linked list in the input is shown.
After flattening the multilevel linked list it becomes:

Input: head = [1,2,null,3]
Output: [1,3,2]
Explanation: The multilevel linked list in the input is shown.
After flattening the multilevel linked list it becomes:

Input: head = []
Output: []
Explanation: There could be empty list in the input.
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""


class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        current = head

        while current:
            if current.child:
                self.merge(current)

            current = current.next
        return head

    def merge(self, node):
        child = node.child

        while child.next:
            child = child.next

        if node.next:
            child.next = node.next
            node.next.prev = child

        node.next = node.child
        node.child.prev = node
        node.child = None
