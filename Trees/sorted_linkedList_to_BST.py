"""
Author: Soumil Ramesh Kulkarni
Date: 01/24/2024

Question: Given a linked list with elements sorted in ascending order, convert it into a height-balanced binary search tree.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedListToBST_helper(self, sorted_list, start, end):
        if start > end:
            return None
        mid = start + (end - start) // 2
        root = TreeNode(val=sorted_list[mid])
        root.left = self.sortedListToBST_helper(sorted_list, start, mid - 1)
        root.right = self.sortedListToBST_helper(sorted_list, mid + 1, end)
        return root

    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        sorted_list = []
        while head:
            sorted_list.append(head.val)
            head = head.next

        if sorted_list:
            return self.sortedListToBST_helper(sorted_list, 0, len(sorted_list) - 1)
        else:
            return None

