"""
Author: Soumil Ramesh Kulkarni
Date: 02/03/2024

Question:
Given a linked list, find its middle element.

If the list has even number of nodes, return the second of the two middle nodes.


Eg:
{
"head": [1, 2, 3, 4, 5]
}
output: 3

{
"head": [1, 2, 3, 4]
}
output: 3

Constraints:

0 <= number of nodes <= 105
-2 * 109 <= node value <= 2 * 109
Do it in one pass over the list
If given linked list is empty, return null.
"""

"""
For your reference:
class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None
"""


def find_middle_node(head):
    """
    Args:
     head(LinkedListNode_int32)
    Returns:
     LinkedListNode_int32
    """
    # Write your code here.
    if head is None or head.next is None:
        return head
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow
