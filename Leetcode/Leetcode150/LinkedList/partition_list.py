"""
Author: Soumil Ramesh Kulkarni
Date: 02.19.2024

Question:
Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

Example 1:
Input: head = [1,4,3,2,5,2], x = 3
Output: [1,2,2,4,3,5]

Example 2:
Input: head = [2,1], x = 2
Output: [1,2]
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        lessDummy = ListNode(0)
        lessTail = lessDummy

        greaterDummy = ListNode(0)
        greaterTail = greaterDummy

        current = head
        while current:
            if current.val < x:
                lessTail.next = current
                lessTail = current
            else:
                greaterTail.next = current
                greaterTail = current
            current = current.next

            # Terminate the greater Tail
        greaterTail.next = None

        # Attach the greater list to the lesser list
        lessTail.next = greaterDummy.next

        return lessDummy.next
