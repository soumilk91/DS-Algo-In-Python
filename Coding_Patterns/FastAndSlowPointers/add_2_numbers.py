"""
Author: Soumil Ramesh Kulkarni
Date: 03.30.2024

Question:
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order,
and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.



Example 1:


Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # get the first number
        first_number = 0
        runner = l1
        power = 0
        while runner:
            first_number += runner.val * (10 ** power)
            power += 1
            runner = runner.next

        # get the second number
        second_number = 0
        runner = l2
        power = 0
        while runner:
            second_number += runner.val * (10 ** power)
            power += 1
            runner = runner.next

        final_number = first_number + second_number

        temp = ListNode(0)
        if final_number == 0:
            return temp
        runner = temp
        while final_number > 0:
            remainder = final_number % 10
            runner.next = ListNode(remainder)
            runner = runner.next
            final_number = final_number // 10
        return temp.next