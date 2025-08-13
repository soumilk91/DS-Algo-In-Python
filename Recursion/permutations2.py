"""
Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.



Example 1:

Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]
Example 2:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
"""

from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # Sort to make it easy to skip duplicates
        result = []
        used = [False] * len(nums)  # Track which elements are used

        def backtrack(slate):
            if len(slate) == len(nums):
                result.append(slate[:])
                return

            for i in range(len(nums)):
                # Skip used numbers
                if used[i]:
                    continue
                # Skip duplicates in the same recursive level
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue

                used[i] = True
                slate.append(nums[i])
                backtrack(slate)
                slate.pop()
                used[i] = False

        backtrack([])
        return result
