"""
Author: Soumil Rmaesh Kulkarni
Date: 03.30.2024

Question:
We have n jobs, where every job is scheduled to be done from startTime[i] to endTime[i], obtaining a profit of profit[i].

You're given the startTime, endTime and profit arrays, return the maximum profit you can take such that there are no two
jobs in the subset with overlapping time range.

If you choose a job that ends at time X you will be able to start another job that starts at time X.



Example 1:



Input: startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]
Output: 120
Explanation: The subset chosen is the first and fourth job.
Time range [1-3]+[3-6] , we get profit of 120 = 50 + 70.
Example 2:



Input: startTime = [1,2,3,4,6], endTime = [3,5,10,6,9], profit = [20,20,100,70,60]
Output: 150
Explanation: The subset chosen is the first, fourth and fifth job.
Profit obtained 150 = 20 + 70 + 60.
Example 3:



Input: startTime = [1,1,1], endTime = [2,3,4], profit = [5,6,4]
Output: 6
"""

import heapq
class Solution:
    def jobScheduling(self, starts, ends, profits):
        start, end, profit = 0, 1, 2
        jobs = list(zip(starts, ends, profits))
        jobs.sort(key=lambda x: x[start])

        heap = []
        max_profit = 0

        for i in range(len(jobs)):
            while heap and heap[0][0] <= jobs[i][start]:
                max_profit = max(max_profit, heapq.heappop(heap)[1])
            heapq.heappush(heap, (jobs[i][end], jobs[i][profit] + max_profit))

        while heap:
            max_profit = max(max_profit, heapq.heappop(heap)[1])

        return max_profit