"""
Author: Soumil Ramesh Kulkarni:
Date: 03.02.2024

Question:
Given head which is a reference node to a singly-linked list. The value of each node in the linked list is either 0 or 1. The linked list holds the binary representation of a number.

Return the decimal value of the number in the linked list.

The most significant bit is at the head of the linked list.



Example 1:


Input: head = [1,0,1]
Output: 5
Explanation: (101) in base 2 = (5) in base 10
Example 2:

Input: head = [0]
Output: 0

"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: ListNode
        :rtype: int
        """
        binary_str = ""
        current = head
        while current != None:
            binary_str += str(current.val)
            current = current.next
        return int(binary_str, 2)


    # Better Solution
    def getDecimalValue_better_solution(self, head):
        """
        :type head: ListNode
        :rtype: int
        """
        answer = 0
        while head:
            answer = 2*answer + head.val
            head = head.next
        return answer