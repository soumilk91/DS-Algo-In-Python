"""
Question:
You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as
directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time
it takes for a signal to travel from source to target.

We will send a signal from a given node k. Return the minimum time it takes for all the n nodes to receive the signal.
If it is impossible for all the n nodes to receive the signal, return -1.



Example 1:


Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
Output: 2
Example 2:

Input: times = [[1,2,1]], n = 2, k = 1
Output: 1
Example 3:

Input: times = [[1,2,1]], n = 2, k = 2
Output: -1
"""

from collections import deque, defaultdict
from typing import *
import heapq


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Create a Graph
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        minHeap = [(0, k)]
        visited = set()
        resultTime = 0
        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in visited:
                continue
            visited.add(n1)
            resultTime = max(resultTime, w1)
            for nei, neiWeight in graph[n1]:
                if nei not in visited:
                    heapq.heappush(minHeap, (neiWeight + w1, nei))
        if len(visited) == n:
            return resultTime
        else:
            return -1