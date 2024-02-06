"""
Author: Soumil Ramesh Kulkarni
Date: 02/03/2024

Question:
Remove n-th node from the end of the given linked list. Return the head of the modified list.

Eg:
{
"n": 2,
"head": [0, 1, 10, 5, 7]
}
output: [0, 1, 10, 7]

{
"n": 1,
"head": [7]
}
output: []

Notes
Constraints:

1 <= length of the list <= 105
1 <= n <= length of the list
-109 <= value in a list node <= 109

"""

"""
For your reference:
class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None
"""


def remove_nth_node_from_end(n, head):
    """
    Args:
     n(int32)
     head(LinkedListNode_int32)
    Returns:
     LinkedListNode_int32
    """
    # Write your code here.
    if head is None:
        return head

    # Create that gap of n
    runner = head
    for i in range(n - 1):
        runner = runner.next

    prev = None
    current = head
    while runner.next:
        prev = current
        current = current.next
        runner = runner.next

    if prev is None:
        return head.next
    prev.next = current.next
    return head


