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


class Solution:
    def get_middle(self, head):
        if not head or not head.next:
            return head
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def sortedMerge(self, left, right):
        result = None
        if left is None:
            return right
        if right is None:
            return left

        if left.val <= right.val:
            result = left
            result.next = self.sortedMerge(left.next, right)
        else:
            result = right
            result.next = self.sortedMerge(left, right.next)
        return result

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        middle = self.get_middle(head)
        next_to_middle = middle.next

        middle.next = None

        left = self.sortList(head)
        right = self.sortList(next_to_middle)

        return_node = self.sortedMerge(left, right)

        return return_node