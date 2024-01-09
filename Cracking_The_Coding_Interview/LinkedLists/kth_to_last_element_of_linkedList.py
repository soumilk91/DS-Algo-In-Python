"""
Author: Soumil Ramesh Kulkarni
Date: 01/04/2024

Question: Design an algorithm to find the kth to the last element of the linked List
"""

"""
Things to consider here: 
-> Will k be always valid ? For our sake, lets consider YES
-> We can use a two pointer approach to get the last k elements 
for example: if the linked list is : 2 3 4 5 6 7
k = 4
then we should print: 5 6 7 (All the elements after the forth position)


Another question to consider here is the find he last k elements from the linked List. Assuming that k is valid. 
for example: if the Linked List is : 2 3 4 5 6 7
k = 4
then we should print: 4 5 6 7 (The last 4 elements from the Linked List)
"""

def kth_to_last_element(head, k):
    current = head
    # Go to the required position
    for i in range(k - 1):
        current = current.next
    # Iterate over the remainder of the linked List
    while current:
        print(current.data)
        current = current.next


def last_k_elements(head, k):
    start = head
    end = head
    # Create that window of length k
    for i in range(k - 1):
        end = end.next
    # Loop over the entire linked list, making sure to track that window
    while end.next:
        start = start.next
        end = end.next
    # All Elements from start to the end of the linked list from here are the last k elements of the Linked List
    while start:
        print(start.data)
        start = start.next


# Now Lets Test Our Logic for both Codes

from singly_linked_list_basic_functions import *

llobject = LinkedListBasicFunctions()
llobject.insertAtEnd(2)
llobject.insertAtEnd(3)
llobject.insertAtEnd(4)
llobject.insertAtEnd(5)
llobject.insertAtEnd(6)
llobject.insertAtEnd(7)
llobject.iterateOverLinkedList()

print ("Kth to the Last Element =========================")
kth_to_last_element(llobject.head, 4)

print("Last k Elements of the Linked List ====================")
last_k_elements(llobject.head, 4)