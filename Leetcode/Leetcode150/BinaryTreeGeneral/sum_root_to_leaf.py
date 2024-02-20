"""
Author: Soumil Ramesh Kulkarni
Date: 02.19.2024

Question:
You are given the root of a binary tree containing digits from 0 to 9 only.

Each root-to-leaf path in the tree represents a number.

For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.
Return the total sum of all root-to-leaf numbers. Test cases are generated so that the answer will fit in a 32-bit integer.

A leaf node is a node with no children.

Example 1:
Input: root = [1,2,3]
Output: 25
Explanation:
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.
Therefore, sum = 12 + 13 = 25.

Example 2:
Input: root = [4,9,0,5,1]
Output: 1026
Explanation:
The root-to-leaf path 4->9->5 represents the number 495.
The root-to-leaf path 4->9->1 represents the number 491.
The root-to-leaf path 4->0 represents the number 40.
Therefore, sum = 495 + 491 + 40 = 1026.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumNumbers_bfs(self, root: Optional[TreeNode]) -> int:
        # We can Use a BFS Again Here
        if root is None:
            return 0
        result = 0
        queue = [(root, "0")]
        while queue:
            node = queue.pop(0)
            temp = node[1] + str(node[0].val)
            # If at leaf Add the sum to the fina;l Answer
            if node[0].left is None and node[0].right is None:
                result += int(temp)

            if node[0].left:
                queue.append((node[0].left, temp))
            if node[0].right:
                queue.append((node[0].right, temp))
        return result

    def sumNumbers_dfs(self, root: Optional[TreeNode]) -> int:
        # Lets Also Do this Using DFS
        def dfs(node, path_sum):
            if node is None:
                return 0
            path_sum = path_sum * 10 + node.val
            if node.left is None and node.right is None:
                return path_sum

            return dfs(node.left, path_sum) + dfs(node.right, path_sum)

        return dfs(root, 0)

