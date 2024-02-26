"""
Author: Soumil Ramesh Kulkarni
Date: 02.24.2024

Question:
Find Median Of A Sorted Circular Linked List
Given a pointer to an arbitrary node in a sorted circular linked list, find the median value of the elements.

Example One
Example one

Given pointer points to the node with value 4.

Output:

6
The sequence is sorted by value so the median value is the middle node. The answer does not depend on the specific node given as input: as long as the list is as pictured, the answer is 6.

Example Two
Example Two

Given pointer points to the node with value 4.

Output:

5
If the number of nodes is even, the median is the average of two middle values. This list is sorted in the descending order
"""



#For your reference:
class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

def find_median(ptr):
    """
    Args:
     ptr(LinkedListNode_int32)
    Returns:
     int32
    """
    # Write your code here.
    if ptr is None:
        return 0
    if ptr.next == ptr:
        return ptr.value
    runner = ptr
    #runner = runner.next
    temp = []
    while True:
        temp.append(runner.value)
        runner = runner.next
        if runner == ptr:
            break
    #print(temp)
    temp.sort()
    #print(temp)
    if len(temp) % 2 != 0:
        mid = len(temp) // 2
        #print(mid)
        return temp[mid]
    else:
        mid = len(temp) // 2
        mid_minus_1 = mid - 1
        return (temp[mid] + temp[mid_minus_1]) // 2
