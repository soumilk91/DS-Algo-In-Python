"""
Author: Soumil Ramesh Kulkarni
Date: 02.25.2024

Question:
Given a linked list, reverse every group of k nodes. If there is a remainder (a group of less than k nodes) in the end,
 reverse that last group, too.

Example One
{
"head": [1, 2, 3, 4, 5, 6],
"k": 3
}
Output:

[3, 2, 1, 6, 5, 4]
Input list consists of two whole groups of three. In the output list the first three and last three nodes are reversed.

Example Two
{
"head": [1, 2, 3, 4, 5, 6, 7, 8],
"k": 3
}
Output:

[3, 2, 1, 6, 5, 4, 8, 7]
There are two whole groups of three and one partial group (a remainder that consists of just two nodes). Each of the
three groups is reversed in the output.
"""

#For your reference:
class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None


def reverse(start, end):
    prev = None
    while start != end:
        start.next, start, prev = prev, start.next, start
    return prev  # return head node of the reversed group


def reverse_linked_list_in_groups_of_k(head, k):
    """
    Args:
     head(LinkedListNode_int32)
     k(int32)
    Returns:
     LinkedListNode_int32
    """
    # Write your code here.
    if not head:
        return None
    start = head
    end = head
    count = 0
    while end and count < k:
        end = end.next
        count += 1

    new_head = reverse(start, end)
    start.next = reverse_linked_list_in_groups_of_k(end, k)
    return new_head

