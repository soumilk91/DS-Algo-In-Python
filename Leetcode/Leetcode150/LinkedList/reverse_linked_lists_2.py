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
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if not head or left == right:
            return head

        dummy = ListNode(0, head)
        prev = dummy

        # Step 1: Move prev to the node before 'left'
        for _ in range(left - 1):
            prev = prev.next

        # Step 2: Reverse the sublist
        curr = prev.next
        prev_sublist = None
        for _ in range(right - left + 1):
            temp = curr.next
            curr.next = prev_sublist
            prev_sublist = curr
            curr = temp

        # Step 3: Connect reversed sublist with main list
        prev.next.next = curr
        prev.next = prev_sublist

        return dummy.next

