"""
Question:

Given a non-negative integer represented as a linked list of digits, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list.



Example 1:

Input: head = [1,2,3]
Output: [1,2,4]
Example 2:

Input: head = [0]
Output: [1]

"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverse(self, root):
        prev = None
        curr = root
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr= next_node
        return prev

    def plusOne(self, head: ListNode) -> ListNode:
        ll_rev = self.reverse(head)
        runner = ll_rev
        carry = 1
        while runner:
            carry += runner.val
            runner.val = carry % 10
            carry = carry // 10
            if runner.next is None:
                break
            runner = runner.next
        if carry != 0:
            runner.next = ListNode(carry)
        return self.reverse(ll_rev)