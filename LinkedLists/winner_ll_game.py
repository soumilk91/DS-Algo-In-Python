"""
Author: Soumil Ramesh Kulkarni
Date: 03.23.2024

Question:
You are given the head of a linked list of even length containing integers.

Each odd-indexed node contains an odd integer and each even-indexed node contains an even integer.

We call each even-indexed node and its next node a pair, e.g., the nodes with indices 0 and 1 are a pair, the nodes with indices 2 and 3 are a pair, and so on.

For every pair, we compare the values of the nodes in the pair:

If the odd-indexed node is higher, the "Odd" team gets a point.
If the even-indexed node is higher, the "Even" team gets a point.
Return the name of the team with the higher points, if the points are equal, return "Tie".



Example 1:

Input: head = [2,1]

Output: "Even"

Explanation: There is only one pair in this linked list and that is (2,1). Since 2 > 1, the Even team gets the point.

Hence, the answer would be "Even".

Example 2:

Input: head = [2,5,4,7,20,5]

Output: "Odd"

Explanation: There are 3 pairs in this linked list. Let's investigate each pair individually:

(2,5) -> Since 2 < 5, The Odd team gets the point.

(4,7) -> Since 4 < 7, The Odd team gets the point.

(20,5) -> Since 20 > 5, The Even team gets the point.

The Odd team earned 2 points while the Even team got 1 point and the Odd team has the higher points.

Hence, the answer would be "Odd".

Example 3:

Input: head = [4,5,2,1]

Output: "Tie"

Explanation: There are 2 pairs in this linked list. Let's investigate each pair individually:

(4,5) -> Since 4 < 5, the Odd team gets the point.

(2,1) -> Since 2 > 1, the Even team gets the point.

Both teams earned 1 point.

Hence, the answer would be "Tie".
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def gameResult(self, head: Optional[ListNode]) -> str:
        even, odd, cur = 0, 0, head
        while cur:
            if cur.val > cur.next.val:
                even += 1
            else:
                odd += 1
            cur = cur.next.next

        if even > odd:
            return "Even"
        elif odd > even:
            return "Odd"
        else:
            return "Tie"
