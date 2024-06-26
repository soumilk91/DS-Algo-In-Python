"""
Author: Soumil Ramesh Kulkarni
Date: 04.01.2024

Question:
Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a
multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.

Example 1:
Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]

Example 2:
Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head: return
        start = end = head
        # find the k-th node (the end node for the current group)
        for _ in range(k):
            if not end: return head  # not enough items (< k) => remain the order
            end = end.next
        # reverse the current group with k nodes
        newHead = self.reverse(start, end)
        # after reverse start is the end for the group, link it with the next reversed group
        start.next = self.reverseKGroup(end, k)

        return newHead

    # reverse diapason [start:end), end not inclusive
    def reverse(self, start, end):
        prev = None
        while start != end:
            start.next, start, prev = prev, start.next, start
        return prev  # return head node of the reversed group
