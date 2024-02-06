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

#For your reference:
class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None


def add_two_numbers(l_a, l_b):
    """
    Args:
     l_a(LinkedListNode_int32)
     l_b(LinkedListNode_int32)
    Returns:
     LinkedListNode_int32
    """
    # Write your code here.

    first_number = 0
    runner = l_a
    power = 0
    while runner:
        first_number += runner.value * (10 ** power)
        power += 1
        runner = runner.next

    second_number = 0
    runner = l_b
    power = 0
    while runner:
        second_number += runner.value * (10 ** power)
        power += 1
        runner = runner.next

    final_number = first_number + second_number

    return_head = None
    runner = None
    while final_number > 0:
        quotient = final_number % 10
        final_number = final_number // 10
        if return_head is None:
            return_head = LinkedListNode(quotient)
            runner = return_head
        else:
            runner.next = LinkedListNode(quotient)
            runner = runner.next
    return return_head


