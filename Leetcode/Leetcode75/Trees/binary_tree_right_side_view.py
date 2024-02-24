"""
Author: Soumil Ramesh Kulkarni
Date: 01/29/2024

Question:
Given the root of a binary tree,
imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]
Example 2:

Input: root = [1,null,3]
Output: [1,3]
Example 3:

Input: root = []
Output: []
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # Base Case
        return_list = []
        if root is None:
            return return_list

        queue = []
        queue.append(root)
        while queue:
            for i in range(len(queue) - 1):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            right_most_node = queue.pop(0)
            return_list.append(right_most_node.val)
            if right_most_node.left:
                queue.append(right_most_node.left)
            if right_most_node.right:
                queue.append(right_most_node.right)

        return return_list
