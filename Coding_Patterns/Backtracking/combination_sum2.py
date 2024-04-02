"""
Author: Soumil Ramesh Kulkarni
Date: 04.01.2024

Question:
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in
candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.



Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8
Output:
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5
Output:
[
[1,2,2],
[5]
]
"""


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        def backtrack(nums, targetLeft, path):

            if targetLeft == 0:
                res.append(path)
                return

            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i - 1]:
                    continue
                if nums[i] > targetLeft:
                    break
                backtrack(nums[i + 1:], targetLeft - nums[i], path + [nums[i]])

        res = []
        backtrack(sorted(candidates), target, [])
        return res