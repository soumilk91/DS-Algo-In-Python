"""
Author: Soumil Ramesh Kulkarni
Date: 01/08/2024

Question: Find out if the given Linked List is a Palindrome
"""

"""
Assumptions: 
-> The Linked List will always be valid 

Solution: 
-> Reverse the Linked List and compare

-> We can use a stack to check if the Linked List is a palindrome. First insert all the elements in the Linked List inside a stack. 
   Iterate over the linked List while popping elements from the stack and compare if the data is the same. If by the time the 
   elements in the stack are finished and we cannot find any discrepancy, the Linked List is a palindrome. 
   Time: O(N), Space: O(N)

-> Find out the middle of the Linked List using slow and fast pointers. Only put the first half of the Linked List in a stack and the compare. 
   Time: O(N), Space: O(N/2) 
"""

def linked_list_palindrome(head):
    # If there is a single Node in the Linked List
    if head.next is None:
        return True
    # If there are only 2 nodes in the Linked List
    elif head.next.next is None:
        if head.data == head.next.data:
            return True
        else:
            return False
    # If there are more nodes in the Linked List find the middle of the Linked List using 2 pointer approach
    slow = head
    fast = head
    while fast:
        if fast.next:
            slow = slow.next
            fast = fast.next.next
        else:
            break
    middle_node = slow

    # Lets create a stack
    stack = []

    # We need to make sure our solution works for both cases, one when there are even elements in the List and the
    # other when there are odd elements in the Linked List
    runner = head
    while runner != middle_node:
        stack.append(runner.data)
        runner = runner.next

    # Now we have all the elements in the stack
    # We need to go one step ahead if there are odd number of elemnts in the Linked List
    if fast is not None:
        middle_node = middle_node.next

    # Now compare all the elements from the second half of the Linked List and the stack
    while middle_node:
        ll_element = middle_node.data
        stack_element = stack.pop()
        if ll_element != stack_element:
            return False
        middle_node = middle_node.next
    return True


# Now Lets Test Our Code
from singly_linked_list_basic_functions import LinkedListBasicFunctions
#create a Linked List
llobject = LinkedListBasicFunctions()
llobject.insertAtEnd(2)
llobject.insertAtEnd(1)
llobject.insertAtEnd(2)
if linked_list_palindrome(llobject.head):
    print("Given Linked List is a Palindrome")
else:
    print("Not a Palindrome")