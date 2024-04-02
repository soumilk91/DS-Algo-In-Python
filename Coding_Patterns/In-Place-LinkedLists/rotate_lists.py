"""
Author: Soumil Ramesh Kulkarni
Date: 04.01.2024

Question:
Given the head of a linked list, rotate the list to the right by k places.

Example 1:
Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]

Example 2:
Input: head = [0,1,2], k = 4
Output: [2,0,1]
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or head.next == None:
            return head
        length_list = 0
        temp = head
        while temp:
            temp = temp.next
            length_list += 1
        if k <= length_list:
            k = k
        else:
            k = k % length_list
        for i in range(k):
            current = head
            prev = None
            while current.next != None:
                prev = current
                current = current.next
            prev.next = None
            current.next = head
            head = current
        return head
