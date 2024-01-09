"""
Author: Soumil Ramesh Kulkarni
Date: 01/08/2024

Question: Given 2 singly Linked List, determine if they intersect. Return the intersecting Node. Note that the intersection is defind
          based on reference and not value.
"""

"""
Solution:
-> Find out the lengths of the 2 linked List if they are equal, compare the addresses of each element in both linked Lists 
-> If the lengths are different, Increment the starting point of the the longer linked list by the difference between the 2 lengths.
   Compare each element address to check if they intersect 
-> In both cases the first point where the addresses of 2 nodes is the same is the start of the intersection 
-> If no 2 addresses are the same, the Linked Lists never intersect 
"""

def find_if_intersection(head1, head2):
    length_ll1 = 0
    length_ll2 = 0
    # Find the Length of the first Linked List
    temp = head1
    while temp:
        length_ll1 += 1
        temp = temp.next

    # Find the Length of the Second Linked List
    temp1 = head2
    while temp1:
        length_ll2 += 1
        temp = temp.next

    # Compare the two Tails of the given Linked List. If they are different, there is no intersection
    if temp != temp1:
        return None

    # runners for the comparison
    runner1 = head1
    runner2 = head2


    difference = abs(length_ll2 - length_ll1)
    if difference > 0:
        if length_ll2 > length_ll1:
            for i in range(difference):
                runner2 = runner2.next
        else:
            for i in range(difference):
                runner1 = runner1.next

    # Now We can compare Each Element

    while runner1:
        if runner1 == runner2:
            # Found the Intersection
            return runner1
        else:
            runner1 = runner1.next
            runner2 = runner2.next
    return None
