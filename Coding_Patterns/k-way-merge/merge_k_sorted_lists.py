"""
Author: Soumil Ramesh Kulkarni
Date: 04.02.2024

Question:
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.



Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
Example 2:

Input: lists = []
Output: []
Example 3:

Input: lists = [[]]
Output: []
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
import heapq


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = ListNode(val=1)
        current = head
        heap = []
        for list in lists:
            temp = list
            while temp:
                heapq.heappush(heap, (temp.val, temp))
                temp = temp.next

        while heap:
            value, node = heapq.heappop(heap)
            current.next = node
            current = current.next
        return head.next
