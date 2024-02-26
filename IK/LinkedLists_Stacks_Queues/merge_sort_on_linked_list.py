"""
Author: Soumil Ramesh Kulkarni
Date: 02.24.2024

Question:
Perform Merge Sort on Linked List

Example One
{
"head": [0, 1, 10, 7]
}
Output:

[0, 1, 7, 10]
Example Two
{
"head": [1, 2, 3]
}
Output:

[1, 2, 3]
"""

#For your reference:
class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

def get_middle_node(head):
    if head is None:
        return head
    slow = head
    fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    return slow


def sorted_merge(left_node, right_node):
    result = None
    if left_node is None:
        return right_node
    if right_node is None:
        return left_node

    if left_node.value <= right_node.value:
        result = left_node
        result.next = sorted_merge(left_node.next, right_node)
    else:
        result = right_node
        result.next = sorted_merge(left_node, right_node.next)
    return result


def merge_sort(head):
    """
    Args:
     head(LinkedListNode_int32)
    Returns:
     LinkedListNode_int32
    """
    # Write your code here.
    if head is None or head.next is None:
        return head

    middle = get_middle_node(head)
    next_to_middle = middle.next

    middle.next = None

    left = merge_sort(head)
    right = merge_sort(next_to_middle)

    return_head = sorted_merge(left, right)
    return return_head
