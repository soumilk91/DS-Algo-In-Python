"""
Author: Soumil Ramesh Kulkarni
Date: 01/04/2024

Question: Remove Duplicates from an unsorted Singly Linked List. Also Think about how would you solve this problem without using a temporary buffer

"""

"""
Approach: Use a dict to track the elements to make sure we can catch duplicates and then change the next pointers for the elements where we 
          do find a duplicate. 
          Time: O(N), Space: O(N)
          
          If an auxilary data structure is not allowed, use a nested loop to remove duplicates. 
          Time: O(N^2), Space: O(1)
"""

def removeDuplicates(head):
    if (head is None) or head.next is None:
        return head
    prev = None
    current = head
    compare_dict = dict()
    while current:
        if current.data not in compare_dict:
            compare_dict[current.data] = 1
        else:
            prev.next = current.next
        prev = current
        current = current.next
    return head

def removeDuplicatesNestedLoop(head):
    if (head is None) or (head.next is None):
        return head
    outer = head
    while outer.next:
        prev = outer
        current = outer.next
        while current:
            if current.data == outer.data:
                prev.next = current.next
            else:
                pass
            prev = current
            current = current.next
        outer = outer.next
    return head


# Lets Test Our Code from above
from singly_linked_list_basic_functions import *

llobject = LinkedListBasicFunctions()
llobject.insertAtEnd(2)
llobject.insertAtEnd(5)
llobject.insertAtEnd(2)
llobject.insertAtEnd(9)
llobject.insertAtEnd(6)
llobject.insertAtstart(6)
llobject.iterateOverLinkedList()
print("------------------")
#temp = removeDuplicates(llobject.head)
temp = removeDuplicatesNestedLoop(llobject.head)
temp1 = temp
while temp1:
    print(temp1.data)
    temp1 = temp1.next

