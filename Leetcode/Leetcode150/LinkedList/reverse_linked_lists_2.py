"""
Link to the Problem:  https://leetcode.com/problems/reverse-linked-list-ii/description/?envType=study-plan-v2&envId=top-interview-150

Author: Soumil Ramesh Kulkarni
Date: 02.19.2024

Question:
Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list
 from position left to position right, and return the reversed list.

Example 1:
Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]

Example 2:
Input: head = [5], left = 1, right = 1
Output: [5]
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # Base Case
        if head is None or left == right:
            return head

        dummy_node = ListNode(0, head)
        prev = dummy_node

        for i in range(left - 1):
            prev = prev.next

        current = prev.next

        for j in range(right - left):
            new_node = current.next
            current.next = new_node.next
            new_node.next = prev.next
            prev.next = new_node
        return dummy_node.next
