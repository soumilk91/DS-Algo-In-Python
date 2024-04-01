"""
Author: Soumil Ramesh Kulkarni
Date: 03.31.2024

Question:
You are given an integer array nums with no duplicates. A maximum binary tree can be built recursively from nums
using the following algorithm:

Create a root node whose value is the maximum value in nums.
Recursively build the left subtree on the subarray prefix to the left of the maximum value.
Recursively build the right subtree on the subarray suffix to the right of the maximum value.
Return the maximum binary tree built from nums.

Example 1:
Input: nums = [3,2,1,6,0,5]
Output: [6,3,5,null,2,0,null,null,1]
Explanation: The recursive calls are as follow:
- The largest value in [3,2,1,6,0,5] is 6. Left prefix is [3,2,1] and right suffix is [0,5].
    - The largest value in [3,2,1] is 3. Left prefix is [] and right suffix is [2,1].
        - Empty array, so no child.
        - The largest value in [2,1] is 2. Left prefix is [] and right suffix is [1].
            - Empty array, so no child.
            - Only one element, so child is a node with value 1.
    - The largest value in [0,5] is 5. Left prefix is [0] and right suffix is [].
        - Only one element, so child is a node with value 0.
        - Empty array, so no child.

Example 2:
Input: nums = [3,2,1]
Output: [3,null,2,null,1]
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        # We will use a stack to keep track of the nodes we have created so far
        stack = []
        for num in nums:
            node = TreeNode(num)
            # If the stack is not empty and the current number is greater than the top of the stack,
            # we need to pop the stack until we find a node with a value greater than the current number.
            # The last popped node will be the parent of the current node.
            while stack and num > stack[-1].val:
                node.left = stack.pop()

            # If the stack is not empty, the top node is the parent of the current node.
            # We set the right child of the parent to be the current node.
            if stack:
                stack[-1].right = node

            # We push the current node onto the stack.
            stack.append(node)

        # The last node on the stack is the root of the tree.
        return stack[0]