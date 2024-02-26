"""
Author: Soumil Ramesh Kulkarni
Date: 02.24.2024

Question:

You are given a linked list with the continuous sequence of the natural numbers, i.e., 1, 2, ..., n.
Apart from the standard pointer to the next node, each node also has another one pointing to a random node in the list.
Any of these two pointers may be empty (null, nil). The random pointer may point to the node itself or any other node in the list.

Clone the list in an efficient manner, both in terms of time and memory usage.

Example

Output:

Return the head of a new list that is identical to the given list, but includes (reuses) none of the nodes from the
original list: you must create all nodes of the new list
"""

#For your reference:
class LinkedListNode:
    def __init__(self, node_data):
        self.value = node_data
        self.next = None
        self.random = None


def clone_linked_list(head):
    """
    Args:
     head(LinkedListNode)
    Returns:
     LinkedListNode
    """
    # Write your code here.
    new_head = None
    new_tail = None
    temp_head = head
    temp_dict = {}
    while temp_head:
        new_node = LinkedListNode(temp_head.value)
        temp_dict[temp_head] = new_node
        if not new_head:
            new_head = new_node
            new_tail = new_node
        else:
            new_tail.next = new_node
            new_tail = new_tail.next
        temp_head = temp_head.next
    temp_head = head
    temp1_head = new_head
    while temp_head:
        a = temp_head.random
        if temp_head.random:
            temp1_head.random = temp_dict[a]
        else:
            temp1_head.random = None
        temp_head = temp_head.next
        temp1_head = temp1_head.next
    return new_head


