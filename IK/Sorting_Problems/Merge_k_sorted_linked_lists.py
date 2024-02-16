"""
Author: Soumil Ramesh Kulkarni
Date: 02/12/2024

Question:
Given k linked lists where each one is sorted in the ascending order, merge all of them into a single sorted linked list.
Eg:
Input:
{
"lists": [
[1, 3, 5],
[3, 4],
[7]
]
}

Output:
[1, 3, 3, 4, 5, 7]
"""


#For your reference:
class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

import heapq


def merge_k_lists(lists):
    """
    Args:
     lists(list_LinkedListNode_int32)
    Returns:
     LinkedListNode_int32
    """
    # Write your code here.
    head = current = LinkedListNode(0)

    #Initialize a Min Heap
    h = []

    temp = 0
    #Insert all the heads of all given k linkedLists into the min heap
    for i in range(len(lists)):
        if lists[i]:
            heapq.heappush(h, (lists[i].value, temp, lists[i]))
            temp += 1

    while h:
        # while heap is not empty
        # remove the smallest element and attaching the corresponding next pointers
        # if the popped node has a next node, insert it into the Heap
        _, __, node = heapq.heappop(h)
        if node.next:
            temp += 1
            heapq.heappush(h, (node.next.value, temp, node.next))

        current.next = node
        current = current.next

    return head.next
