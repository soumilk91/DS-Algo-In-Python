"""
Author: Soumil Ramesh Kulkarni
Date: 01/09/2024

Question:
Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices,
and return the reordered list.
The first node is considered odd, and the second node is even, and so on.
Note that the relative order inside both the even and odd groups should remain as it was in the input.
You must solve the problem in O(1) extra space complexity and O(n) time complexity.

Eg:

Input: head = [1,2,3,4,5]
Output: [1,3,5,2,4]

Input: head = [2,1,3,5,6,4,7]
Output: [2,3,6,7,1,5,4]

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
Approach: 
-> Use a 2 pointer approach 
-> change the next pointers for the 2 linked Lists 
-> Make sure to remember the head of both odd and even linked Lists 
-> join the 2 heads of the Linked Lists at the last 
"""


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # if the Linked List is empty, has only one node or has only 2 nodes, Do nothing
        if head is None or head.next is None or head.next.next is None:
            return head
        # maintain the head pointers for both the Linked Lists
        odd_head = head
        even_head = head.next
        # Runners to find out the next node for both the Linked Lists
        odd_runner = odd_head
        even_runner = even_head
        while True:
            # Change Pointer for Odd Node
            next_odd_node = odd_runner.next.next
            odd_runner.next = next_odd_node
            # Change Pointer for Even Node
            next_even_node = even_runner.next.next
            even_runner.next = next_even_node
            # Shift the positions of both the odd and even runners
            odd_runner = odd_runner.next
            even_runner = even_runner.next
            # Break if the even_runner.next is None or even_runner itself is None
            if even_runner is None or even_runner.next is None:
                break
        odd_runner.next = even_head
        return odd_head