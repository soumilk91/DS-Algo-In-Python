"""
Author: Soumil Ramesh Kulkarni
Date: 03.22.2024

Question:
You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.

Example 1:
Input: head = [1,2,3,4]
Output: [1,4,2,3]

Example 2:
Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverse(self, head):
        prev = None
        current = head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev

    def merge(self, head1, head2):
        temp = ListNode(0)
        temp_runner = temp
        while head1 and head2:
            temp_runner.next = head1
            head1 = head1.next
            temp_runner = temp_runner.next
            temp_runner.next = head2
            head2 = head2.next
            temp_runner = temp_runner.next
        while head1:
            temp_runner.next = head1
            head1 = head1.next
            temp_runner = temp_runner.next
        while head2:
            temp_runner.next = head2
            head2 = head2.next
            temp_runner = temp_runner.next
        return temp.next

    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return head
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        ll1 = head
        ll2 = slow.next
        slow.next = None
        ll2 = self.reverse(ll2)
        temp_node = ListNode(0)
        temp_node.next = self.merge(ll1, ll2)
        return temp_node.next
