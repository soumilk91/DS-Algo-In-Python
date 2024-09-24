"""
Author: Soumil Ramesh Kulkarni
Date: 03.22.2024

Question:
You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.

Example 1:
Input: head = [1,2,3,4]
Output: [1,4,2,3]

Example 2:
Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import *
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # Base Case. When there are less than 3 nodes in the given Linked List
        if not head or not head.next or not head.next.next:
            return head
        slow = head
        fast = head
        prev = None
        # Find the Middle of the Linked List
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        # Use Stack to keep a track of the reversed Linked List
        prev.next = None
        stack = []
        while slow:
            stack.append(slow)
            slow = slow.next

        # Now change the links of all the Nodes starting from head and until the stack is empty
        # Use a dummyNode to start the result list
        dummy = ListNode(-1)
        runner = dummy
        origRunner = head
        while origRunner or stack:
            if origRunner:
                runner.next = origRunner
                runner = runner.next
                origRunner = origRunner.next

            if stack:
                runner.next = stack.pop()
                runner = runner.next

        # Make sure that the last node in the result list points to Null
        runner.next = None
        return dummy.next
