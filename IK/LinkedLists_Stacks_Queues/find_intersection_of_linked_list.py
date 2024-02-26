"""
Author: Soumil Ramesh Kulkarni
Date: 02.24.2024

Question:

"""


#For your reference:
class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

def find_intersection(l1, l2):
    """
    Args:
     l1(LinkedListNode_int32)
     l2(LinkedListNode_int32)
    Returns:
     int32
    """
    # Write your code here.
    if l1 is None or l2 is None:
        return -1
    temp1 = l1
    temp2 = l2
    countTemp1 = 0
    countTemp2 = 0
    while temp1.next != None:
        countTemp1 += 1
        temp1 = temp1.next
    while temp2.next != None:
        countTemp2 += 1
        temp2 = temp2.next
    if temp1 != temp2:
        return -1
    if countTemp1 == countTemp2:
        temp1 = l1
        temp2 = l2
    elif countTemp1 > countTemp2:
        finalCount = countTemp1 - countTemp2
        temp1 = l1
        for i in range(finalCount):
            temp1 = temp1.next
        temp2 = l2
    else:
        finalCount = countTemp2 - countTemp1
        temp2 = l2
        for i in range(finalCount):
            temp2 = temp2.next
        temp1 = l1
    while temp1:
        if temp1 == temp2:
            return temp1.value
        else:
            temp1 = temp1.next
            temp2 = temp2.next