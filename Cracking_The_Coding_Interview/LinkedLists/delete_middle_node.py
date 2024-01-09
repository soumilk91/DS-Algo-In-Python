"""
Author: Soumil Ramesh Kulkarni
Date: 01/08/2024

Question: Implement an algorithm to delete a node in the middle of the linked List, given only access to that node
Eg:

Given Linked List: 1 -> 2 -> 3 -> 4 -> 5
Given pointer to node : 3
Resultant Linked List Contents: 1-> 2 -> 4 -> 5

"""

"""
Assumptions:
-> The given node cannot be the first or the last node in the linked list 

Solution:
-> Run a while loop from that node to the end of the Linked List copying the next element data in the current node 
-> Time: O(N), Space: O(1) 
"""

def delete_a_node_from_middle(node):
    current = node
    next_node = node.next
    while next_node.next:
        current.data = next_node.data
        current = current.next
        next_node = next_node.next
    current.data = next_node.data
    current.next = None

# Lets test our Function from above
from singly_linked_list_basic_functions import *
def main():
    # Create a Singly Linked List
    llobject = LinkedListBasicFunctions()
    llobject.insertAtEnd(1)
    llobject.insertAtEnd(2)
    llobject.insertAtEnd(3)
    llobject.insertAtEnd(4)
    llobject.insertAtEnd(5)
    llobject.iterateOverLinkedList()
    print("=================")
    # Get the node that we want to delete using the function written above
    temp = llobject.head
    for i in range(2):
        temp = temp.next
    delete_a_node_from_middle(temp)
    print("Print the Linked List after deleting the node")
    llobject.iterateOverLinkedList()


if __name__ == "__main__":
    main()