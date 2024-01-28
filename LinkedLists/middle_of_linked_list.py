"""
Author: Soumil Ramesh Kulkarni
Date: 01/27/2024

Question:
Given a linked list, find its middle element.

If the list has even number of nodes, return the second of the two middle nodes.

eg:
{
"head": [1, 2, 3, 4, 5]
}
output: 3

{
"head": [1, 2, 3, 4]
}
output: 3
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
    while fast and fast.next != None:
        slow = slow.next
        fast = fast.next.next
    return slow
