"""
Author: Soumil Ramesh Kulkarni
Date: 04.03.2024

Question:
You are given the root of a binary tree with n nodes. Each node is assigned a unique value from 1 to n. You are also given an array queries of size m.

You have to perform m independent queries on the tree where in the ith query you do the following:

Remove the subtree rooted at the node with the value queries[i] from the tree. It is guaranteed that queries[i] will not be equal to the value of the root.
Return an array answer of size m where answer[i] is the height of the tree after performing the ith query.

Note:

The queries are independent, so the tree returns to its initial state after each query.
The height of a tree is the number of edges in the longest simple path from the root to some node in the tree.
Input: root = [1,3,4,2,null,6,5,null,null,null,null,null,7], queries = [4]
Output: [2]
Explanation: The diagram above shows the tree after removing the subtree rooted at node with value 4.
The height of the tree is 2 (The path 1 -> 3 -> 2).

Example 2:
Input: root = [5,8,9,2,1,3,7,4,6], queries = [3,2,4,8]
Output: [3,2,3,2]
Explanation: We have the following queries:
- Removing the subtree rooted at node with value 3. The height of the tree becomes 3 (The path 5 -> 8 -> 2 -> 4).
- Removing the subtree rooted at node with value 2. The height of the tree becomes 2 (The path 5 -> 8 -> 1).
- Removing the subtree rooted at node with value 4. The height of the tree becomes 3 (The path 5 -> 8 -> 2 -> 6).
- Removing the subtree rooted at node with value 8. The height of the tree becomes 2 (The path 5 -> 9 -> 3).
"""

import heapq
from collections import defaultdict
from typing import Optional, List

import
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        node_to_lvl = {}
        lvls = defaultdict(list)

        def dfs(node, height):
            if not node:
                return 0
            height += 1
            left = dfs(node.left, height) + 1
            right = dfs(node.right, height) + 1
            node_to_lvl[node.val] = height
            heapq.heappush(lvls[height], (-max(left, right) - height + 1, height, node.val))
            return max(left, right)

        dfs(root, -1)
        res = []

        for q in queries:
            lvl = node_to_lvl[q]
            if q == root.val:
                res.append(0)
            elif len(lvls[lvl]) == 1:
                res.append(lvls[lvl - 1][0][1])
            elif lvls[lvl][0][2] == q:
                temp = heapq.heappop(lvls[lvl])
                res.append(-lvls[lvl][0][0])
                heapq.heappush(lvls[lvl], temp)
            elif lvls[lvl][0][2] != q:
                res.append(-lvls[lvl][0][0])

        return res