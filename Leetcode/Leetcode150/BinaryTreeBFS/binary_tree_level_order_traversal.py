"""
Author: Soumil Ramesh Kulkarni
Date: 02.18.2024

Question:
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
Input: root = [1]
Output: [[1]]

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        return_list = []
        queue = collections.deque()
        queue.append(root)
        while queue:
            temp_list = []
            queue_length = len(queue)
            for i in range(queue_length):
                pop_element = queue.popleft()
                if pop_element:
                    temp_list.append(pop_element.val)
                    queue.append(pop_element.left)
                    queue.append(pop_element.right)
            if temp_list:
                return_list.append(temp_list)
        return return_list

