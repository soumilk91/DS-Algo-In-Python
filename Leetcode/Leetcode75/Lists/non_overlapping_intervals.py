"""
Author: Soumil Ramesh Kulkarni
Date: 03.30.2024

Question:
Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you
need to remove to make the rest of the intervals non-overlapping.



Example 1:

Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.
Example 2:

Input: intervals = [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.
Example 3:

Input: intervals = [[1,2],[2,3]]
Output: 0
Explanation: You don't need to remove any of the intervals since they're already non-overlapping.
"""

from typing import *
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        removal = 0
        temp = []
        if not intervals:
            return removal
        intervals.sort(key=lambda x: x[1])
        for interval in intervals:
            if not temp:
                temp.append(interval)
            else:
                if interval[0] >= temp[-1][1]:
                    temp.append(interval)
                else:
                    removal += 1
        print(temp)
        return removal