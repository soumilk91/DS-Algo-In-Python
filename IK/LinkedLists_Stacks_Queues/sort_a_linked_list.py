"""
Author: Soumil Ramesh Kulkarni
Date: 02.24.2024

Question:
Sort a given Linked List
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


import heapq
def sort_linked_list(head):
    """
    Args:
     head(LinkedListNode_int32)
    Returns:
     LinkedListNode_int32
    """
    # Write your code here.
    if not head:
        return head
    maxHeap = []
    runner = head
    while runner:
        heapq.heappush(maxHeap, [runner.value, runner])
        runner = runner.next
    temp = LinkedListNode(0)
    runner = temp
    while maxHeap:
        a = heapq.heappop(maxHeap)
        runner.next = a[1]
        runner = runner.next
    runner.next = None
    return temp.next
