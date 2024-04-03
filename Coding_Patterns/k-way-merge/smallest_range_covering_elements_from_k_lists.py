"""
Author: Soumil Ramesh Kulkarni
Date: 04.02.2024

Question:
You have k lists of sorted integers in non-decreasing order. Find the smallest range that includes at
least one number from each of the k lists.

We define the range [a, b] is smaller than range [c, d] if b - a < d - c or a < c if b - a == d - c.



Example 1:

Input: nums = [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]
Output: [20,24]
Explanation:
List 1: [4, 10, 15, 24,26], 24 is in range [20,24].
List 2: [0, 9, 12, 20], 20 is in range [20,24].
List 3: [5, 18, 22, 30], 22 is in range [20,24].
Example 2:

Input: nums = [[1,2,3],[1,2,3],[1,2,3]]
Output: [1,1]

"""


class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:

        n = len(nums)

        pq = []
        ma = float('-inf')

        for i in range(n):
            heappush(pq, (nums[i][0], i, 0))
            ma = max(ma, nums[i][0])

        ans = [pq[0][0], ma]
        while True:

            _, i, j = heappop(pq)

            if j == len(nums[i]) - 1:
                break

            next_num = nums[i][j + 1]

            ma = max(ma, next_num)

            heappush(pq, (next_num, i, j + 1))

            if ma - pq[0][0] < ans[1] - ans[0]:
                ans = [pq[0][0], ma]
        return ans