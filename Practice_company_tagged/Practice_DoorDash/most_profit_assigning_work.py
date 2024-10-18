"""
You have n jobs and m workers. You are given three arrays: difficulty, profit, and worker where:

difficulty[i] and profit[i] are the difficulty and the profit of the ith job, and
worker[j] is the ability of jth worker (i.e., the jth worker can only complete a job with difficulty at most worker[j]).
Every worker can be assigned at most one job, but one job can be completed multiple times.

For example, if three workers attempt the same job that pays $1, then the total profit will be $3. If a worker
cannot complete any job, their profit is $0.
Return the maximum profit we can achieve after assigning the workers to the jobs.



Example 1:

Input: difficulty = [2,4,6,8,10], profit = [10,20,30,40,50], worker = [4,5,6,7]
Output: 100
Explanation: Workers are assigned jobs of difficulty [4,4,6,6] and they get a profit of [20,20,30,30] separately.
Example 2:

Input: difficulty = [85,47,57], profit = [24,66,99], worker = [40,25,25]
Output: 0
"""

from typing import *
class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        # Pair each job's difficulty with its corresponding profit
        jobs = list(zip(difficulty, profit))

        # Sort the jobs by difficulty, and in case of ties, by profit
        jobs.sort()

        # Sort the worker array
        worker.sort()

        # Variables to keep track of the total profit and the best job profit we can assign
        total_profit = 0
        best_profit = 0
        job_index = 0
        n = len(jobs)

        # Go through each worker
        for w in worker:
            # While the worker's ability is greater than or equal to the job's difficulty,
            # update the best profit we can get for this worker.
            while job_index < n and jobs[job_index][0] <= w:
                best_profit = max(best_profit, jobs[job_index][1])
                job_index += 1

            # Add the best profit possible for this worker to the total profit
            total_profit += best_profit

        return total_profit