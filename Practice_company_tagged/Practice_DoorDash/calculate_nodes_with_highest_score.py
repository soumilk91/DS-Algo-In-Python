"""
There is a binary tree rooted at 0 consisting of n nodes. The nodes are labeled from 0 to n - 1.
You are given a 0-indexed integer array parents representing the tree, where parents[i] is the parent of node i.
Since node 0 is the root, parents[0] == -1.

Each node has a score. To find the score of a node, consider if the node and the edges connected to it were removed.
The tree would become one or more non-empty subtrees. The size of a subtree is the number of the nodes in it.
The score of the node is the product of the sizes of all those subtrees.

Return the number of nodes that have the highest score.


Example 1:
Input: parents = [-1,2,0,2,0]
Output: 3
Explanation:
- The score of node 0 is: 3 * 1 = 3
- The score of node 1 is: 4 = 4
- The score of node 2 is: 1 * 1 * 2 = 2
- The score of node 3 is: 4 = 4
- The score of node 4 is: 4 = 4
The highest score is 4, and three nodes (node 1, node 3, and node 4) have the highest score.

Example2:
Input: parents = [-1,2,0]
Output: 2
Explanation:
- The score of node 0 is: 2 = 2
- The score of node 1 is: 2 = 2
- The score of node 2 is: 1 * 1 = 1
The highest score is 2, and two nodes (node 0 and node 1) have the highest score.
"""

from typing import *
class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        n = len(parents)
        tree = [[] for _ in range(n)]

        # Build the tree structure
        for i in range(1, n):
            tree[parents[i]].append(i)

        # Array to store the size of each subtree
        subtree_size = [0] * n

        # DFS to calculate subtree sizes
        def dfs(node):
            size = 1  # Count the node itself
            for child in tree[node]:
                size += dfs(child)  # Add the sizes of its children
            subtree_size[node] = size
            return size

        # Start DFS from the root (node 0)
        dfs(0)

        max_score = 0
        count = 0

        # Calculate the score for each node
        for i in range(n):
            score = 1
            total_size = n

            # For each child of node i, multiply by the size of the child's subtree
            for child in tree[i]:
                score *= subtree_size[child]
                total_size -= subtree_size[child]

            # If there's a parent subtree (the rest of the tree), include its size
            if i != 0:
                score *= total_size - 1  # Remaining nodes outside this node's subtree

            # Update the maximum score and count the number of nodes with the max score
            if score > max_score:
                max_score = score
                count = 1
            elif score == max_score:
                count += 1

        return count
