"""
Author: Soumil Ramesh Kulkarni
Date: 01/08/2024

Question: Given a Circular Linked List, implement an algorithm that return the start of the loop.
Followup: What if we need to detect if there is a loop
"""

def detect_loop(head):
    # Use the 2 pointer Approach
    slow = head
    fast = head
    if_loop_present = None
    while fast:
        if fast.next:
            slow= slow.next
            fast = fast.next.next
            if slow == fast:
                if_loop_present = slow
                break
        else:
            # There is no Loop present
            return None
    if if_loop_present:
        temp1 = head
        temp2 = if_loop_present
        while temp1 != temp2:
            temp1 = temp1.next
            temp2 = temp2.next
        return temp1
    else:
        return None
