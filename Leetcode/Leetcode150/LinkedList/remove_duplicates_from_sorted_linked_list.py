"""
Author: Soumil Ramesh Kulkarni
Date: 02.19.2024

Question:
Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from
 the original list. Return the linked list sorted as well.

Example 1:
Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]

Example 2:
Input: head = [1,1,1,2,3]
Output: [2,3]

"""

"""
Approach
Create a dummy node dummy and set its next node as the head of the linked list.
Create a prev variable and initialize it with dummy.
Use a while loop to traverse the linked list while head and head.next are not None.
Check if the value of the current node head is equal to the value of the next node head.next.
If yes, then use another while loop to traverse the linked list and find all the duplicates.
Once all the duplicates are found, set head to head.next and update the next node of prev to head.
If the values are not equal, update the prev to prev.next and head to head.next.
Return dummy.next as the new head of the linked list.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import *
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1, head)
        runner = dummy
        while head:
            if head.next and head.val == head.next.val:
                while head.next and head.val == head.next.val:
                    head = head.next

                runner.next = head.next
            else:
                runner = runner.next

            head = head.next
        return dummy.next
