"""
Author: Soumil Ramesh Kulkarni
Date: 01/09/2024

Question:
In a linked list of size n, where n is even, the ith node (0-indexed) of the linked list is known as the twin of the (n-1-i)th node, if 0 <= i <= (n / 2) - 1.

For example, if n = 4, then node 0 is the twin of node 3, and node 1 is the twin of node 2. These are the only nodes with twins for n = 4.
The twin sum is defined as the sum of a node and its twin.

Given the head of a linked list with even length, return the maximum twin sum of the linked list.

Eg:
Input: head = [5,4,2,1]
Output: 6
Explanation:
Nodes 0 and 1 are the twins of nodes 3 and 2, respectively. All have twin sum = 6.
There are no other nodes with twins in the linked list.
Thus, the maximum twin sum of the linked list is 6.

Input: head = [4,2,2,3]
Output: 7
Explanation:
The nodes with twins present in this linked list are:
- Node 0 is the twin of node 3 having a twin sum of 4 + 3 = 7.
- Node 1 is the twin of node 2 having a twin sum of 2 + 2 = 4.
Thus, the maximum twin sum of the linked list is max(7, 4) = 7.

Input: head = [1,100000]
Output: 100001
Explanation:
There is only one node with a twin in the linked list having twin sum of 1 + 100000 = 100001.

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
Approach: 
-> Divide the Linked List into 2 parts. 
-> Push all the elements in the second part of the Linked List into a stack 
-> add all the elements from the start of the Linked List with the top of the stack and keep popping after every operation 
-> Keep a track of the max sum while doing the above step 
-> return this max sum variable 
-> Time: O(N), Space: O(N/2)
"""
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        stack = []
        slow = head
        fast = head
        while fast:
            slow = slow.next
            fast = fast.next.next
        while slow:
            stack.append(slow.val)
            slow = slow.next
        runner = head
        max_sum = 0
        while stack:
            temp = runner.val + stack.pop()
            if temp > max_sum:
                max_sum = temp
            runner = runner.next
        return max_sum