"""
Author: Soumil Ramesh Kulkarni
Date: 03.19.2024

Question:
Given the head of a linked list, return the list after sorting it in ascending order.

Example 1:
Input: head = [4,2,1,3]
Output: [1,2,3,4]

Example 2:
Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]

Example 3:
Input: head = []
Output: []
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


import heapq
from typing import *
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        runner = head
        min_heap = []
        while runner:
            heapq.heappush(min_heap, (runner.val, runner))
            runner = runner.next

        temp_node = ListNode(0)
        runner = temp_node
        while min_heap:
            val, node = heapq.heappop(min_heap)
            runner.next = node
            runner = runner.next
        if runner:
            runner.next = None
        return temp_node.next