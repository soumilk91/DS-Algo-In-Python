"""
Author: Soumil Ramesh Kulkarni
Date: 03.25.2024

Question:
Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of
conference rooms required.



Example 1:

Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2
Example 2:

Input: intervals = [[7,10],[2,4]]
Output: 1
"""
import heapq
from typing import *
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        heap = []
        intervals.sort()
        for interval in intervals:
            if not heap or heap[0] > interval[0]:
                heapq.heappush(heap, interval[1])
            else:
                heapq.heapreplace(heap, interval[1])
        return len(heap)
