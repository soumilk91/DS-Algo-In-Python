"""
Author: Soumil Ramesh Kulkarni
Date: 01/27/2024

Question:
Given a linked list, zip it from its two ends in place, using constant extra space.
The nodes in the resulting zipped linked list should go in this order: first, last, second, second last, and so on.

Follow up:

Implement functions to zip two linked lists and to unzip such that unzip(zip(L1, L2)) returns L1 and L2.

Eg:
{
"head": [1, 2, 3, 4, 5, 6]
}
output: [1, 6, 2, 5, 3, 4]

{
"head": [1, 2, 3, 4, 5]
}
output:[1, 5, 2, 4, 3]
"""

"""
For your reference:
class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None
"""


def reverse_linkedList(head):
    """
    Function to reverse the singly singly linked List
    """
    prev = None
    current = head
    while current:
        new_node = current.next
        current.next = prev
        prev = current
        current = new_node
    return prev


def zip_given_linked_list(head):
    """
    Args:
     head(LinkedListNode_int32)
    Returns:
     LinkedListNode_int32
    """
    # Write your code here.
    if head is None or head.next is None or head.next.next is None:
        return head
    slow = head
    prev = None
    fast = head

    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next

    if fast is None:
        head1 = head
        prev.next = None
        head2 = reverse_linkedList(slow)
    else:
        head1 = head
        temp = slow.next
        slow.next = None
        head2 = reverse_linkedList(temp)

    return merge_linked_lists(head1, head2)


def merge_linked_lists(head1, head2):
    temp1 = head1
    temp2 = head2
    prev = None

    while temp1 and temp2:
        # Get the next nodes for both linked Lists
        temp1_next_node = temp1.next
        if temp2.next == None:
            prev = temp2
        temp2_next_node = temp2.next

        # Change the next pointers
        temp1.next = temp2
        temp2.next = temp1_next_node

        # change the value of temp1 and temp2
        temp1 = temp1_next_node
        temp2 = temp2_next_node

    if temp1:
        prev.next = temp1
    return head1