"""
Author: Soumil Ramesh Kulkarni
Date: 03.13.2024

Question:
Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.

Example 1:
Input: head = [1,2,6,3,4,5,6], val = 6
Output: [1,2,3,4,5]
Example 2:

Input: head = [], val = 1
Output: []
Example 3:

Input: head = [7,7,7,7], val = 7
Output: []
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return None
        current = head
        prev = None
        while current:
            if current.val == val:
                if current == head:
                    current = current.next
                    head = current
                else:
                    prev.next = current.next
                    current = prev.next
            else:
                prev = current
                current = current.next
        return head
