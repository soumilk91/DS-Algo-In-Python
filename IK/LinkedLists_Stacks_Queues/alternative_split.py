"""
Author: Soumil Ramesh Kulkarni
Date: 02/05/2024

Question:
Given a linked list, split it into two by alternating nodes: first node goes into the first list,
second to second, third to first, fourth to second and so on.

Eg:
{
"head": [1, 2, 3, 4, 5]
}
Output:
[
[1, 3, 5],
[2, 4]
]
"""


#For your reference:
class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None


def alternative_split(head):
    """
    Args:
     head(LinkedListNode_int32)
    Returns:
     list_LinkedListNode_int32
    """
    # Write your code here.
    head1 = LinkedListNode(0)
    head1runner = head1
    head2 = LinkedListNode(0)
    head2runner = head2
    if head is None:
        return [None, None]
    if head.next is None:
        return [head, None]
    count = 1
    while head:
        if count % 2 != 0:
            head1runner.next = LinkedListNode(head.value)
            head1runner = head1runner.next
        else:
            head2runner.next = LinkedListNode(head.value)
            head2runner = head2runner.next
        head = head.next
        count += 1
    return [head1.next, head2.next]


