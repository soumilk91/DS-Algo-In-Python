"""
There is an undirected graph with n nodes numbered from 0 to n - 1 (inclusive). You are given a 0-indexed integer array
values where values[i] is the value of the ith node. You are also given a 0-indexed 2D integer array edges, where each
edges[j] = [uj, vj, timej] indicates that there is an undirected edge between the nodes uj and vj, and it takes timej
seconds to travel between the two nodes. Finally, you are given an integer maxTime.

A valid path in the graph is any path that starts at node 0, ends at node 0, and takes at most maxTime seconds to complete.
You may visit the same node multiple times. The quality of a valid path is the sum of the values of the unique nodes
visited in the path (each node's value is added at most once to the sum).

Return the maximum quality of a valid path.

Note: There are at most four edges connected to each node.

Example1:
Input: values = [0,32,10,43], edges = [[0,1,10],[1,2,15],[0,3,10]], maxTime = 49
Output: 75
Explanation:
One possible path is 0 -> 1 -> 0 -> 3 -> 0. The total time taken is 10 + 10 + 10 + 10 = 40 <= 49.
The nodes visited are 0, 1, and 3, giving a maximal path quality of 0 + 32 + 43 = 75.

Example2:
Input: values = [5,10,15,20], edges = [[0,1,10],[1,2,10],[0,3,10]], maxTime = 30
Output: 25
Explanation:
One possible path is 0 -> 3 -> 0. The total time taken is 10 + 10 = 20 <= 30.
The nodes visited are 0 and 3, giving a maximal path quality of 5 + 20 = 25.

Example3:
Input: values = [1,2,3,4], edges = [[0,1,10],[1,2,11],[2,3,12],[1,3,13]], maxTime = 50
Output: 7
Explanation:
One possible path is 0 -> 1 -> 3 -> 1 -> 0. The total time taken is 10 + 13 + 13 + 10 = 46 <= 50.
The nodes visited are 0, 1, and 3, giving a maximal path quality of 1 + 2 + 4 = 7.
"""

from collections import defaultdict
from typing import *
class Solution:
    def maximalPathQuality(self, values: List[int], edges: List[List[int]], maxTime: int) -> int:

        # Build graph from edges
        graph = defaultdict(list)
        for u, v, t in edges:
            graph[u].append((v, t))
            graph[v].append((u, t))

        # Initialize max_quality to store the best path quality
        max_quality = 0

        def dfs(node, time_left, current_quality, visited):
            nonlocal max_quality

            # Update the max quality if we've returned to node 0
            if node == 0:
                max_quality = max(max_quality, current_quality)

            # Explore each neighbor of the current node
            for neighbor, travel_time in graph[node]:
                if time_left >= travel_time:  # Only explore if we have enough time
                    # Track the visited node and add its value to the path's quality if it's a first visit
                    first_visit = neighbor not in visited
                    if first_visit:
                        visited.add(neighbor)
                        current_quality += values[neighbor]

                    # Perform DFS on the neighbor node
                    dfs(neighbor, time_left - travel_time, current_quality, visited)

                    # Backtrack: undo the changes to current_quality and visited
                    if first_visit:
                        current_quality -= values[neighbor]
                        visited.remove(neighbor)

        # Start DFS from node 0
        dfs(0, maxTime, values[0], set([0]))

        return max_quality