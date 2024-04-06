"""
Author: Soumil Ramesh Kulkarni
Date: 04.03.2024

Question:
Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the
minimum number of conference rooms required.



Example 1:

Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2
Example 2:

Input: intervals = [[7,10],[2,4]]
Output: 1
"""
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        h =[]
        sort = sorted(intervals)
        for i in sort:
            # need a new meeting room
            if h == [] or h[0] >i[0]:
                heapq.heappush(h,i[1])
            # don't need a new meeting room, just update the end time
            else:
                heapq.heapreplace(h,i[1])
        return len(h)