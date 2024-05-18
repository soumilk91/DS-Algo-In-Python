"""
Author: Soumil Ramesh Kulkarni
Date: 05.18.2024

Question:
A split of an integer array is good if:

The array is split into three non-empty contiguous subarrays - named left, mid, right respectively from left to right.
The sum of the elements in left is less than or equal to the sum of the elements in mid, and the sum of
the elements in mid is less than or equal to the sum of the elements in right.
Given nums, an array of non-negative integers, return the number of good ways to split nums. As the number
may be too large, return it modulo 109 + 7.



Example 1:

Input: nums = [1,1,1]
Output: 1
Explanation: The only good way to split nums is [1] [1] [1].
Example 2:

Input: nums = [1,2,2,2,5,0]
Output: 3
Explanation: There are three good ways of splitting nums:
[1] [2] [2,2,5,0]
[1] [2,2] [2,5,0]
[1,2] [2,2] [5,0]
Example 3:

Input: nums = [3,2,1]
Output: 0
Explanation: There is no good way to split nums.
"""

from typing import *
class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        prefix = [0]
        for x in nums: prefix.append(prefix[-1] + x)

        ans = j = k = 0
        for i in range(1, len(nums)):
            j = max(j, i + 1)
            while j < len(nums) and 2 * prefix[i] > prefix[j]: j += 1
            k = max(k, j)
            while k < len(nums) and 2 * prefix[k] <= prefix[i] + prefix[-1]: k += 1
            ans += k - j
        return ans % 1_000_000_007