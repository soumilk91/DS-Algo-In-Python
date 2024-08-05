"""
Author: Soumil Ramesh Kulkarni
Date: 03.22.2024

Question:
Given the root of a binary tree, the value of a target node target, and an integer k, return an array of the values of all nodes that have a distance k from the target node.

You can return the answer in any order.

Example 1:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, k = 2
Output: [7,4,1]
Explanation: The nodes that are a distance 2 from the target node (with value 5) have values 7, 4, and 1.

Example 2:
Input: root = [1], target = 1, k = 3
Output: []
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # recursively add a parent pointer to each node
        def add_parent(current, parent):
            if current:
                current.parent = parent
                add_parent(current.left, current)
                add_parent(current.right, current)

        add_parent(root, None)

        answer = []
        visited = set()

        def dfs(node, distance):
            if not node or node in visited:
                return
            visited.add(node)
            if distance == 0:
                answer.append(node.val)
                return

            dfs(node.parent, distance - 1)
            dfs(node.left, distance - 1)
            dfs(node.right, distance - 1)

        dfs(target, k)

        return answer