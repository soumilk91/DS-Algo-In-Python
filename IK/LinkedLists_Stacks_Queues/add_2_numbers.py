"""
Author: Soumil Ramesh Kulkarni
Date: 02/04/2024

Question:
Write a function which adds two numbers a and b, represented as linked lists of size lenA and lenB respectively,
and returns the sum of a and b in the form of a new linked list.

Ignoring the allocation of a new linked list, try to use constant memory when solving it.

A number is represented by a linked list, with the head of the linked list being the least significant digit.
 For example 125 is represented as 5->2->1, and 371 is represented as 1->7->3.
Adding 5->2->1(125) and 1->7->3(371) should produce 6->9->4(496).

Eg:
{
"l_a": [7, 5, 2],
"l_b": [2, 0, 3]
}
output: [9, 5, 5]

{
"l_a": [5, 8, 3],
"l_b": [9, 4, 1]
}
output: [4, 3, 5]
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


# Another Approach
# This is Faster 
def add_two_numbers_carry_approach(l_a, l_b):
    """
    Args:
     l_a(LinkedListNode_int32)
     l_b(LinkedListNode_int32)
    Returns:
     LinkedListNode_int32
    """
    # Write your code here.
    # Get the First Number  Both the Numbers
    dummy = cur =LinkedListNode(0)
    carry = 0
    while l_a or l_b or carry:
        if l_a:
            carry += l_a.value
            l_a = l_a.next
        if l_b:
            carry += l_b.value
            l_b = l_b.next
        cur.next = LinkedListNode(carry%10)
        cur = cur.next
        carry //=10
    return dummy.next