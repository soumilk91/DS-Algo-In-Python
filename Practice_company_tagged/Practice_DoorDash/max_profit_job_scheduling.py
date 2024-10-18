"""
We have n jobs, where every job is scheduled to be done from startTime[i] to endTime[i], obtaining a profit of profit[i].

You're given the startTime, endTime and profit arrays, return the maximum profit you can take such that there are no two
jobs in the subset with overlapping time range.

If you choose a job that ends at time X you will be able to start another job that starts at time X.


Example 1:
Input: startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]
Output: 120
Explanation: The subset chosen is the first and fourth job.
Time range [1-3]+[3-6] , we get profit of 120 = 50 + 70.
"""

from typing import *
import heapq
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:

        result = 0

        jobs = [(beg, end, profit) for beg, end, profit in zip(startTime, endTime, profit)]
        jobs.sort()

        heap = []
        curr_profit = 0

        for beg, end, p in jobs:
            while heap and heap[0][0] <= beg:
                _, prev_profit = heapq.heappop(heap)
                curr_profit = max(curr_profit, prev_profit)

            heapq.heappush(heap, (end, curr_profit + p))

            result = max(result, curr_profit + p)

        return result