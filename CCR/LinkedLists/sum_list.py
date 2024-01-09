"""
Author: Soumil Ramesh Kulkarni
Date: 01/08/2024

Question: You have 2 numbers represented by a Linked List where each node contains a single Digit. the digits are stored in a reverse
          order such that the 1's digit is at the head of the linked List. Write a function to add these 2 numbers and return the result
          as a Linked List
eg:
input (7 -> 1 -> 6) + (5 -> 9 -> 2) = 617 + 295 = 912
output: (2 -> 1 -> 9)

Followup Question: What if the digits are stored in the forward order.
eg:
input: (6 -> 1 -> 7) + (2 -> 9 -> 5) = 617 + 295 = 912
output: (9 -> 1 -> 2)
"""

"""
Solution: 
For the followup find out the length of the first and the second linked list to make sure we can give the power correctly 

Time: O(N), Space: O(1)
"""
from singly_linked_list_basic_functions import *

def sum_list_reverse(head1, head2):
    first_number = 0
    second_number = 0
    temp = head1
    # calculate the first number
    order = 0
    while temp:
        first_number += temp.data * 10**order
        temp = temp.next
        order += 1
    print("First Number:",first_number)

    # calculate the Second Number
    order = 0
    temp = head2
    while temp:
        second_number += temp.data * 10**order
        temp = temp.next
        order += 1
    print("Second Number:", second_number)

    # Add the 2 numbers
    final_number = first_number + second_number
    print("Final Sum: ", final_number)

    # create a new Linked List to return
    return_linked_list = LinkedListBasicFunctions()

    # Keep dividing the quotient until it is equal to 0
    quotient = final_number
    while quotient != 0:
        remainder = quotient % 10
        return_linked_list.insertAtEnd(remainder)
        quotient = quotient // 10
    return return_linked_list.head



# Lets test Our code for reverse
llobject = LinkedListBasicFunctions()
llobject.insertAtEnd(7)
llobject.insertAtEnd(1)
llobject.insertAtEnd(6)

llobject2=LinkedListBasicFunctions()
llobject2.insertAtEnd(5)
llobject2.insertAtEnd(9)
llobject2.insertAtEnd(2)

result = sum_list_reverse(llobject.head, llobject2.head)
temp = result
print("Resultant Linked List: ")
while temp:
    print(temp.data)
    temp = temp.next